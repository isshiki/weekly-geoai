"""Check built HTML references and generated history text fragments, offline."""
import argparse
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote, urljoin, urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]
BLOCKS = set('p div li td th h1 h2 h3 h4 h5 h6 tr br pre section article'.split())


def normalize(text):
    return ' '.join(text.split())


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.links, self.ids, self.parts = [], set(), []
        self.hidden = 0
        self.feed(source)
        self.text = normalize(''.join(self.parts))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        if tag == 'a' and attrs.get('name'):
            self.ids.add(attrs['name'])
        for key in ('href', 'src'):
            if attrs.get(key):
                self.links.append(attrs[key])
        if tag in ('script', 'style'):
            self.hidden += 1
        if tag in BLOCKS:
            self.parts.append(' ')

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.hidden = max(0, self.hidden - 1)
        if tag in BLOCKS:
            self.parts.append(' ')

    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(data)


def fragment_problem(text, directive):
    """Support generator's text=exact and text=start,end, splitting before decode."""
    for item in directive.split('&'):
        if not item.startswith('text='):
            return 'unsupported fragment directive'
        raw = item[5:].split(',')
        if len(raw) not in (1, 2) or raw[0].endswith('-') or raw[-1].startswith('-'):
            return 'unsupported text fragment syntax'
        terms = [normalize(unquote(term)) for term in raw]
        if not all(terms):
            return 'empty text fragment'
        start = text.find(terms[0])
        if start < 0 or (len(terms) == 2 and text.find(terms[1], start) < 0):
            return 'text fragment not found in order'
    return None


def check(site, site_url, history_date=None):
    site = site.resolve()
    files = sorted(site.rglob('*.html'))
    if not files:
        raise ValueError('No built HTML; run mkdocs build first')
    pages = {p: Page(p.read_text(encoding='utf-8')) for p in files}
    histories = {p: re.fullmatch(r'updates/(\d{4}-\d{2}-\d{2})/index.html', p.relative_to(site).as_posix()) for p in files}
    dates = [m[1] for m in histories.values() if m]
    selected = history_date or (max(dates) if dates else None)
    if selected and selected not in dates:
        raise ValueError(f'History page missing: {selected}')
    base = urlsplit(site_url.rstrip('/') + '/')
    errors, warnings = [], []
    fragment_count = 0
    for source, page in pages.items():
        relative = source.relative_to(site).as_posix()
        source_url = urljoin(site_url.rstrip('/') + '/', relative)
        for link in set(page.links):
            url = urlsplit(urljoin(source_url, link))
            if url.scheme not in ('http', 'https') or url.netloc != base.netloc:
                continue
            path = unquote(url.path)
            if not path.startswith(base.path):
                continue  # Same host, another project.
            target = (site / path[len(base.path):]).resolve()
            label = f'{relative} -> {url.path}'
            if not target.is_relative_to(site):
                errors.append(f'{label}: outside site')
                continue
            if target.is_dir():
                target /= 'index.html'
            if not target.is_file():
                errors.append(f'{label}: missing file')
                continue
            if target not in pages or not url.fragment:
                continue
            anchor, separator, directive = url.fragment.partition(':~:')
            if anchor and unquote(anchor) not in pages[target].ids:
                errors.append(f'{label}: missing anchor {unquote(anchor)}')
            if separator:
                fragment_count += 1
                problem = fragment_problem(pages[target].text, directive)
                if problem:
                    history = histories[source]
                    output = warnings if history and history[1] < selected else errors
                    output.append(f'{label}: {problem}')
    return errors, warnings, len(files), fragment_count, selected


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site-dir', type=Path, default=ROOT / 'site')
    parser.add_argument('--history-date', help='Strict history date; default: latest built history')
    args = parser.parse_args()
    config = yaml.safe_load((ROOT / 'mkdocs.yml').read_text(encoding='utf-8'))
    try:
        errors, warnings, count, fragments, selected = check(args.site_dir, config['site_url'], args.history_date)
    except ValueError as error:
        parser.error(str(error))
    for severity, messages in (('ERROR', errors), ('WARNING', warnings)):
        for message in messages:
            print(f'{severity}: {message}')
    print(f'HTML={count}; text-fragment links={fragments}; strict history={selected}; errors={len(errors)}; historical warnings={len(warnings)}')
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())
