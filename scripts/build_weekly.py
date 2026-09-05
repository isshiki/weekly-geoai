from __future__ import annotations

import argparse
import re
from collections import OrderedDict
from dataclasses import dataclass, field
from datetime import date, timedelta
from pathlib import Path

from common import REPO_ROOT, configured_path, issue_title, parse_front_matter


@dataclass
class DailyItem:
    url: str
    title: str = ""
    sources: list[tuple[date, str]] = field(default_factory=list)


def _parse_daily(path: Path, source_date: date) -> list[DailyItem]:
    items: list[DailyItem] = []
    current: DailyItem | None = None
    for line in path.read_text(encoding="utf-8").splitlines():
        url_match = re.match(r"^- URL: <(https?://.+)>$", line)
        if url_match:
            current = DailyItem(url=url_match.group(1), sources=[(source_date, "")])
            items.append(current)
            continue
        if current is None:
            continue
        title_match = re.match(r"^  - タイトル:\s*(.*)$", line)
        if title_match:
            current.title = title_match.group(1).strip()
            continue
        note_match = re.match(r"^  - 一言:\s*(.*)$", line)
        if note_match:
            current.sources[-1] = (source_date, note_match.group(1).strip())
    return items


def collect_items(publication_date: date, root: Path = REPO_ROOT) -> list[DailyItem]:
    if publication_date.weekday() != 4:
        raise ValueError("発行日は金曜日を指定してください")
    daily_dir = configured_path("GEOAI_DAILY_DIR", "daily", root)
    period_start = publication_date - timedelta(days=7)
    merged: OrderedDict[str, DailyItem] = OrderedDict()
    for offset in range(7):
        source_date = period_start + timedelta(days=offset)
        path = daily_dir / f"{source_date.isoformat()}.md"
        if not path.exists():
            continue
        for item in _parse_daily(path, source_date):
            if item.url not in merged:
                merged[item.url] = item
            else:
                existing = merged[item.url]
                if not existing.title and item.title:
                    existing.title = item.title
                existing.sources.extend(item.sources)
    return list(merged.values())


def next_issue_number(root: Path = REPO_ROOT) -> int:
    candidates = [configured_path("GEOAI_DRAFT_DIR", "drafts", root)]
    numbers: list[int] = []
    for directory in candidates:
        if not directory.exists():
            continue
        for path in directory.glob("????-??-??.md"):
            try:
                metadata, _ = parse_front_matter(path.read_text(encoding="utf-8"))
                numbers.append(int(metadata["issue_number"]))
            except (KeyError, OSError, ValueError):
                continue
    return max(numbers, default=0) + 1


def _render_items(items: list[DailyItem]) -> str:
    blocks: list[str] = []
    for index, item in enumerate(items, start=1):
        notes = []
        for source_date, note in item.sources:
            safe_note = note.replace("--", "—")
            notes.append(f"{source_date.isoformat()}: {safe_note}" if safe_note else source_date.isoformat())
        source_note = "\n".join(notes)
        title = item.title or "タイトル要確認"
        blocks.append(
            f"<!-- source-note\n{source_note}\n-->\n"
            f"### {index}. [{title}](<{item.url}>)\n\n"
            "［紹介文を1〜2文で記入］"
        )
    return "\n\n".join(blocks)


def build(
    publication_date: date,
    *,
    issue_number: int | None = None,
    force: bool = False,
    root: Path = REPO_ROOT,
) -> Path:
    if publication_date.weekday() != 4:
        raise ValueError("発行日は金曜日を指定してください")
    items = collect_items(publication_date, root)
    if not items:
        raise ValueError("対象となる前週金曜から木曜の日次URLがありません")
    number = issue_number if issue_number is not None else next_issue_number(root)
    if number < 1:
        raise ValueError("号数は1以上を指定してください")

    draft_dir = configured_path("GEOAI_DRAFT_DIR", "drafts", root)
    draft_dir.mkdir(parents=True, exist_ok=True)
    output = draft_dir / f"{publication_date.isoformat()}.md"
    if output.exists() and not force:
        raise FileExistsError(f"下書きが既にあります: {output}")

    template = (root / "editorial" / "weekly-template.md").read_text(encoding="utf-8")
    replacements = {
        "{{issue_number}}": str(number),
        "{{publication_date}}": publication_date.isoformat(),
        "{{issue_title}}": issue_title(number, publication_date),
        "{{items}}": _render_items(items),
    }
    content = template
    for key, value in replacements.items():
        content = content.replace(key, value)
    output.write_text(content.rstrip() + "\n", encoding="utf-8")
    return output


def _default_friday(today: date | None = None) -> date:
    today = today or date.today()
    return today + timedelta(days=(4 - today.weekday()) % 7)


def main() -> int:
    parser = argparse.ArgumentParser(description="日次メモから週刊GeoAIの下書きを作る")
    parser.add_argument("--date", type=date.fromisoformat, default=_default_friday())
    parser.add_argument("--issue-number", type=int)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    try:
        output = build(
            args.date,
            issue_number=args.issue_number,
            force=args.force,
        )
    except (FileExistsError, OSError, ValueError) as exc:
        parser.error(str(exc))
    print(f"下書きを作成しました: {output.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
