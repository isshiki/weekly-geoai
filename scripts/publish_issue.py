from __future__ import annotations

import argparse
import html
import re
import shutil
from datetime import date
from pathlib import Path

from common import (
    COMMENTARY_PLACEHOLDERS,
    DEFINITION,
    INTRO_PLACEHOLDER,
    REPO_ROOT,
    SUBTITLE_PLACEHOLDER,
    configured_path,
    issue_title,
    parse_front_matter,
    remove_source_comments,
)


ITEM_HEADING = re.compile(r"^### (\d+)\. \[(.+)\]\(<(https?://.+)>\)$", re.MULTILINE)
IMAGE = re.compile(r"^!\[([^\]]+)\]\(([^\s)]+)\)$", re.MULTILINE)


def _paragraphs(text: str) -> list[str]:
    return [" ".join(block.splitlines()).strip() for block in re.split(r"\n\s*\n", text) if block.strip()]


def _sentence_count(text: str) -> int:
    return len(re.findall(r"[。！？](?:[」』】）)]*)", text))


def validate(metadata: dict[str, str], body: str) -> tuple[int, date, str]:
    try:
        number = int(metadata["issue_number"])
        publication_date = date.fromisoformat(metadata["publication_date"])
    except (KeyError, ValueError) as exc:
        raise ValueError("issue_numberまたはpublication_dateが不正です") from exc
    if number < 1 or publication_date.weekday() != 4:
        raise ValueError("号数は1以上、発行日は金曜日である必要があります")

    subtitle = metadata.get("subtitle", "").strip()
    if not subtitle or subtitle == SUBTITLE_PLACEHOLDER:
        raise ValueError("サブタイトルを記入してください")
    if len(subtitle) > 60:
        raise ValueError("サブタイトルは60文字以内にしてください")

    expected_title = issue_title(number, publication_date)
    clean = remove_source_comments(body).strip()
    if not clean.startswith(f"# {expected_title}\n"):
        raise ValueError(f"タイトルは「{expected_title}」にしてください")
    for placeholder in (*COMMENTARY_PLACEHOLDERS, INTRO_PLACEHOLDER):
        if placeholder in clean:
            raise ValueError(f"プレースホルダが残っています: {placeholder}")
    if "タイトル要確認" in clean or "要確認" in clean:
        raise ValueError("要確認の項目が残っています")
    if f"\n{DEFINITION}\n" not in f"\n{clean}\n":
        raise ValueError("定義文が変更または削除されています")

    definition_index = clean.find(DEFINITION)
    before_definition = clean[:definition_index]
    title_end = before_definition.find("\n")
    intro_blocks = _paragraphs(before_definition[title_end + 1 :])
    if len(intro_blocks) != 2:
        raise ValueError("定義文の前には所感をちょうど2段落置いてください")

    matches = list(ITEM_HEADING.finditer(clean))
    if not matches:
        raise ValueError("ニュース＆記事がありません")

    item_numbers = [int(match.group(1)) for match in matches]
    if item_numbers != list(range(1, len(matches) + 1)):
        raise ValueError("ニュース＆記事の番号は1からの連番にしてください")

    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(clean)
        section = clean[start:end].split("\n## ", 1)[0]
        blocks = _paragraphs(section)
        introduction = " ".join(b for b in blocks if not IMAGE.fullmatch(b) and not (b.startswith('*') and b.endswith('*') and not b.startswith('**')))
        count = _sentence_count(introduction)
        news_format = metadata.get('editorial_format') == 'news-v1'
        preceding_sections = re.findall(r'^## (.+)$', clean[:match.start()], re.MULTILINE)
        prominent = preceding_sections and preceding_sections[-1] == '今週の注目ニュース'
        maximum = 6 if news_format and prominent else 2
        if not 1 <= count <= maximum:
            raise ValueError(
                f"「{match.group(2)}」の紹介文は句点で終わる1〜{maximum}文にしてください（現在{count}文）"
            )
    if len(IMAGE.findall(clean)) > 2:
        raise ValueError('画像は1号あたり2枚以内にしてください')
    return number, publication_date, expected_title


def _render_inline(value: str) -> str:
    if value.startswith('*') and value.endswith('*') and not value.startswith('**'):
        return '<em>' + _render_inline(value[1:-1]) + '</em>'
    if '**' in value:
        parts = re.split(r'(\*\*.+?\*\*)', value)
        if len(parts) > 1:
            return ''.join('<strong>' + _render_inline(p[2:-2]) + '</strong>' if p.startswith('**') and p.endswith('**') else _render_inline(p) for p in parts)
    result: list[str] = []
    position = 0
    link_pattern = r"\[([^\]]+)\]\((?:<(https?://[^>]+)>|(https?://[^)]+))\)"
    for match in re.finditer(link_pattern, value):
        result.append(html.escape(value[position : match.start()]))
        label = html.escape(match.group(1))
        href = html.escape(match.group(2) or match.group(3), quote=True)
        result.append(f'<a href="{href}">{label}</a>')
        position = match.end()
    result.append(html.escape(value[position:]))
    return "".join(result)


def markdown_to_substack_html(body: str) -> str:
    clean = remove_source_comments(body).strip()
    output = ["<article>"]
    paragraph: list[str] = []

    def flush() -> None:
        if paragraph:
            value = " ".join(part.strip() for part in paragraph)
            output.append(f"  <p>{_render_inline(value)}</p>")
            paragraph.clear()

    for line in clean.splitlines():
        if not line.strip():
            flush()
            continue
        image = IMAGE.fullmatch(line)
        if image:
            flush()
            output.append(f'  <p><img src="{html.escape(image.group(2), quote=True)}" alt="{html.escape(image.group(1), quote=True)}" style="max-width:100%;height:auto"></p>')
            continue
        heading = re.match(r"^(#{1,3})\s+(.+)$", line)
        if heading:
            flush()
            level = len(heading.group(1))
            output.append(f"  <h{level}>{_render_inline(heading.group(2))}</h{level}>")
        else:
            paragraph.append(line)
    flush()
    output.append("</article>")
    return "\n".join(output) + "\n"


def publish(draft: Path, *, force: bool = False, root: Path = REPO_ROOT) -> Path:
    text = draft.read_text(encoding="utf-8")
    metadata, body = parse_front_matter(text)
    _, publication_date, _ = validate(metadata, body)
    clean_body = remove_source_comments(body).strip() + "\n"

    substack_dir = configured_path("GEOAI_SUBSTACK_DIR", "substack", root)
    substack_dir.mkdir(parents=True, exist_ok=True)
    stem = publication_date.isoformat()
    substack_path = substack_dir / f"{stem}.html"
    if substack_path.exists() and not force:
        raise FileExistsError(f"出力が既にあります: {substack_path}")

    # Resolve every image before writing output. Local assets are uploaded separately in Substack.
    image_files = []
    for index, match in enumerate(IMAGE.finditer(clean_body), 1):
        source = (draft.parent / match.group(2)).resolve()
        if not source.is_relative_to((root / 'drafts' / 'assets').resolve()):
            raise ValueError('画像はdrafts/assets内のローカルファイルを指定してください')
        if source.suffix.lower() not in {'.png', '.jpg', '.jpeg', '.webp'} or not source.is_file():
            raise ValueError(f'画像ファイルが不正または存在しません: {match.group(2)}')
        relative = f'assets/{stem}/{index}{source.suffix.lower()}'
        image_files.append((source, substack_dir / relative))
        clean_body = clean_body.replace(match.group(0), f'![{match.group(1)}]({relative})')
    for source, destination in image_files:
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)

    substack_path.write_text(markdown_to_substack_html(clean_body), encoding="utf-8")
    return substack_path


def main() -> int:
    parser = argparse.ArgumentParser(description="確認済み原稿をSubstack貼り付け用HTMLへ出力する")
    parser.add_argument("draft", type=Path)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    draft = args.draft if args.draft.is_absolute() else REPO_ROOT / args.draft
    try:
        substack_path = publish(draft, force=args.force)
    except (FileExistsError, OSError, ValueError) as exc:
        parser.error(str(exc))
    metadata, _ = parse_front_matter(draft.read_text(encoding="utf-8"))
    print(f"Substackサブタイトル: {metadata['subtitle']}")
    print(f"Substack: {substack_path.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
