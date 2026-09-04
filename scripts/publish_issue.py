from __future__ import annotations

import argparse
import html
import json
import re
from datetime import date
from pathlib import Path

from common import (
    COMMENTARY_PLACEHOLDERS,
    DEFINITION,
    INTRO_PLACEHOLDER,
    REPO_ROOT,
    configured_path,
    issue_title,
    parse_front_matter,
    remove_source_comments,
)


ITEM_HEADING = re.compile(r"^### \[(.+)\]\(<(https?://.+)>\)$", re.MULTILINE)


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
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(clean)
        introduction = " ".join(_paragraphs(clean[start:end]))
        count = _sentence_count(introduction)
        if count not in {1, 2}:
            raise ValueError(
                f"「{match.group(1)}」の紹介文は句点で終わる1〜2文にしてください（現在{count}文）"
            )
    return number, publication_date, expected_title


def _render_inline(value: str) -> str:
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


def _update_archive(index_path: Path, title: str, filename: str) -> None:
    content = index_path.read_text(encoding="utf-8")
    start_marker = "<!-- ISSUES:START -->"
    end_marker = "<!-- ISSUES:END -->"
    if start_marker not in content or end_marker not in content:
        raise ValueError("docs/issues/index.mdの更新マーカーがありません")
    current = re.search(
        rf"{re.escape(start_marker)}\n(.*)\n{re.escape(end_marker)}",
        content,
        flags=re.DOTALL,
    )
    if current is None:
        raise ValueError("docs/issues/index.mdの更新範囲が不正です")
    lines = [line for line in current.group(1).splitlines() if line.startswith("- [")]
    new_line = f"- [{title}](./{filename}.html)"
    lines = [line for line in lines if not line.endswith(f"(./{filename}.html)")]
    lines.append(new_line)

    def sort_key(line: str) -> str:
        match = re.search(r"\./(\d{4}-\d{2}-\d{2})\.html", line)
        return match.group(1) if match else ""

    replacement = "\n".join(sorted(lines, key=sort_key, reverse=True))
    updated = content[: current.start(1)] + replacement + content[current.end(1) :]
    index_path.write_text(updated, encoding="utf-8")


def publish(draft: Path, *, force: bool = False, root: Path = REPO_ROOT) -> tuple[Path, Path]:
    text = draft.read_text(encoding="utf-8")
    metadata, body = parse_front_matter(text)
    number, publication_date, title = validate(metadata, body)
    clean_body = remove_source_comments(body).strip() + "\n"

    public_dir = configured_path("GEOAI_PUBLIC_DIR", "docs/issues", root)
    substack_dir = configured_path("GEOAI_SUBSTACK_DIR", "substack", root)
    public_dir.mkdir(parents=True, exist_ok=True)
    substack_dir.mkdir(parents=True, exist_ok=True)
    stem = publication_date.isoformat()
    public_path = public_dir / f"{stem}.md"
    substack_path = substack_dir / f"{stem}.html"
    existing = [path for path in (public_path, substack_path) if path.exists()]
    if existing and not force:
        joined = ", ".join(str(path) for path in existing)
        raise FileExistsError(f"出力が既にあります: {joined}")

    front_matter = (
        "---\n"
        "layout: default\n"
        f"title: {json.dumps(title, ensure_ascii=False)}\n"
        f"issue_number: {number}\n"
        f"date: {publication_date.isoformat()}\n"
        "---\n\n"
    )
    public_path.write_text(front_matter + clean_body, encoding="utf-8")
    substack_path.write_text(markdown_to_substack_html(clean_body), encoding="utf-8")
    _update_archive(public_dir / "index.md", title, stem)
    return public_path, substack_path


def main() -> int:
    parser = argparse.ArgumentParser(description="確認済み原稿をPages用MarkdownとSubstack用HTMLへ出力する")
    parser.add_argument("draft", type=Path)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    draft = args.draft if args.draft.is_absolute() else REPO_ROOT / args.draft
    try:
        public_path, substack_path = publish(draft, force=args.force)
    except (FileExistsError, OSError, ValueError) as exc:
        parser.error(str(exc))
    print(f"Pages: {public_path.relative_to(REPO_ROOT)}")
    print(f"Substack: {substack_path.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
