"""Maintain dated Atlas review links and year/month history indexes.

Run with the site's Python environment (Markdown and PyYAML are required).
Before committing daily edits: --date YYYY-MM-DD --base HEAD
Existing review links are preserved unless that date is explicitly requested.
"""
from __future__ import annotations

import argparse
import re
import subprocess
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import quote

import markdown
import yaml

ROOT = Path(__file__).resolve().parents[1]
START = "<!-- atlas-review:start -->"
END = "<!-- atlas-review:end -->"


def git(*args: str) -> str:
    result = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, encoding="utf-8")
    if result.returncode:
        raise RuntimeError(result.stderr.strip())
    return result.stdout


def snapshot(ref: str, path: str) -> str:
    # A missing file is expected for a newly created Atlas page.
    if path not in git("ls-tree", "-r", "--name-only", ref, "--", path).splitlines():
        return ""
    return git("show", f"{ref}:{path}")


class Blocks(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.items: list[str] = []
        self.stack: list[tuple[str, list[str]]] = []

    def handle_starttag(self, tag, attrs):
        if tag in {"p", "li", "td", "th"}:
            self.stack.append((tag, []))

    def handle_data(self, data):
        for _, parts in self.stack:
            parts.append(data)

    def handle_endtag(self, tag):
        if self.stack and self.stack[-1][0] == tag:
            _, parts = self.stack.pop()
            text = " ".join("".join(parts).split())
            if text:
                self.items.append(text)


def blocks(source: str) -> list[str]:
    source = re.sub(r"\A---\n.*?\n---\n", "", source, flags=re.S)
    # Sources and related links are not the substantive change under review.
    source = re.split(r"^## (?:出典|関連項目)\s*$", source, flags=re.M)[0]
    parser = Blocks()
    parser.feed(markdown.markdown(source, extensions=["tables", "fenced_code", "md_in_html"]))
    return list(dict.fromkeys(parser.items))


def encode(text: str) -> str:
    return quote(text, safe="").replace("-", "%2D")


def review_link(path: str, current: str, before: str, after: str, site_url: str):
    title = yaml.safe_load(current.split("---", 2)[1])["title"]
    old = set(blocks(before))
    live = set(blocks(current))
    changed = [b for b in blocks(after) if b not in old and b in live and len(b) >= 12]
    # Every retained changed block is highlighted, including separate paragraphs.
    directives = []
    if not before and changed:
        # A new page is one contiguous review range, not a huge list of fragments.
        directives.append("text=" + encode(changed[0]) + "," + encode(changed[-1]))
        changed = []
    for text in changed:
        value = encode(text)
        directives.append("text=" + value)
    url = site_url.rstrip("/") + "/" + path.removeprefix("docs/").removesuffix(".md") + "/"
    state = "新規" if not before else "更新"
    if directives:
        url += "#:~:" + "&".join(directives)
    else:
        state += "・本文変更後のためページ全体"
    return f"- [{title}]({url}) — {state}"


def add_review(day: Path, base: str | None, site_url: str) -> None:
    source = day.read_text(encoding="utf-8")
    source = re.sub(re.escape(START) + r".*?" + re.escape(END) + r"\n*", "", source, flags=re.S)
    relative = day.relative_to(ROOT).as_posix()
    if base:
        end = None
        beginning = base
    else:
        revisions = git("log", "--reverse", "--format=%H", "--", relative).splitlines()
        end = revisions[-1]
        beginning = revisions[0] + "^"
    targets = list(dict.fromkeys("docs/" + p for p in re.findall(r"\]\(\.\./(atlas/[^)#]+\.md)(?:#[^)]*)?\)", source)))
    # Include supplemental page edits even if the news item links to another page.
    diff_args = (beginning, end) if end else (beginning,)
    for path in git("diff", "--name-only", *diff_args, "--", "docs/atlas").splitlines():
        file = ROOT / path
        if file.suffix == ".md" and file.exists() and f"updated: {day.stem}" in file.read_text(encoding="utf-8"):
            if path not in targets and path != "docs/atlas/index.md":
                targets.append(path)
    links = []
    for path in targets:
        file = ROOT / path
        if not file.exists():
            continue
        current = file.read_text(encoding="utf-8")
        before = snapshot(beginning, path)
        after = snapshot(end, path) if end else current
        if before == after:
            continue
        links.append(review_link(path, current, before, after, site_url))
    section = START + "\n## 変更したAtlasページ\n\n"
    section += "この一覧を選択して一括で開くと、Atlasページだけを確認できる。同じページは1回にまとめている。対応ブラウザーでは変更した文章をハイライトする。後日の改稿で文章が一致しなくなった場合はハイライトされない。\n\n"
    section += "\n".join(links) if links else "この日のAtlas本文の変更はない。"
    section += "\n" + END + "\n\n"
    position = source.find("\n## ")
    if position < 0:
        source = source.rstrip() + "\n\n" + section
    else:
        source = source[:position] + "\n\n" + section + source[position + 1:]
    day.write_text(source, encoding="utf-8")


def indexes(config: dict) -> None:
    days = sorted((ROOT / "docs/updates").glob("????-??-??.md"), reverse=True)
    years = sorted({p.stem[:4] for p in days}, reverse=True)
    history = [{"一覧": "updates/index.md"}]
    root_text = "---\ntitle: 更新履歴\n---\n\n# 更新履歴\n\n日別ページの冒頭に、変更したAtlasページだけのリンク集を掲載している。\n\n"
    for year in years:
        months = sorted({p.stem[5:7] for p in days if p.stem.startswith(year)}, reverse=True)
        root_text += f"- [{year}年]({year}/index.md)\n"
        year_nav = [{"年の一覧": f"updates/{year}/index.md"}]
        year_text = f"---\ntitle: {year}年の更新履歴\n---\n\n# {year}年の更新履歴\n\n"
        for month in months:
            subset = [p for p in days if p.stem.startswith(f"{year}-{month}")]
            year_text += f"- [{int(month)}月]({month}/index.md)\n"
            month_text = f"---\ntitle: {year}年{int(month)}月の更新履歴\n---\n\n# {year}年{int(month)}月の更新履歴\n\n"
            month_nav = [{"月の一覧": f"updates/{year}/{month}/index.md"}]
            for day in subset:
                label = f"{int(month)}月{int(day.stem[-2:])}日"
                month_text += f"- [{label}](../../{day.name})\n"
                month_nav.append({label: f"updates/{day.name}"})
            folder = ROOT / f"docs/updates/{year}/{month}"
            folder.mkdir(parents=True, exist_ok=True)
            (folder / "index.md").write_text(month_text, encoding="utf-8")
            year_nav.append({f"{int(month)}月": month_nav})
        (ROOT / f"docs/updates/{year}/index.md").write_text(year_text, encoding="utf-8")
        history.append({f"{year}年": year_nav})
    (ROOT / "docs/updates/index.md").write_text(root_text, encoding="utf-8")
    path = ROOT / "mkdocs.yml"
    source = path.read_text(encoding="utf-8")
    replacement = yaml.safe_dump([{"更新履歴": history}], allow_unicode=True, sort_keys=False, width=120)
    replacement = "\n".join("  " + line for line in replacement.rstrip().splitlines()) + "\n"
    source = re.sub(r"^  - 更新(?:記録|履歴):\n.*?(?=^  - |^plugins:)", replacement, source, flags=re.S | re.M)
    path.write_text(source, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date")
    parser.add_argument("--base", default="HEAD")
    parser.add_argument("--backfill", action="store_true")
    args = parser.parse_args()
    config = yaml.safe_load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"))
    for day in sorted((ROOT / "docs/updates").glob("????-??-??.md")):
        if day.stem == args.date:
            add_review(day, args.base, config["site_url"])
        elif args.backfill and START not in day.read_text(encoding="utf-8"):
            add_review(day, None, config["site_url"])
    indexes(config)


if __name__ == "__main__":
    main()
