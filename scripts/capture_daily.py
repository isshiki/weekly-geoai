from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

from common import REPO_ROOT, configured_path


def _one_line(value: str) -> str:
    return " / ".join(part.strip() for part in value.splitlines() if part.strip())


def _field(label: str, value: str) -> str:
    normalized = _one_line(value)
    return f"  - {label}: {normalized}" if normalized else f"  - {label}:"


def _validate_url(url: str) -> None:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError("URLはhttpまたはhttpsの完全なURLを指定してください")
    if "<" in url or ">" in url:
        raise ValueError("URLに < または > は使用できません")


def capture(
    url: str,
    *,
    note: str = "",
    title: str = "",
    kind: str = "",
    topics: str = "",
    summary: str = "",
    atlas_path: str = "",
    entry_date: date | None = None,
    root: Path = REPO_ROOT,
) -> tuple[Path, bool]:
    _validate_url(url)
    entry_date = entry_date or date.today()
    daily_dir = configured_path("GEOAI_DAILY_DIR", "daily", root)
    daily_dir.mkdir(parents=True, exist_ok=True)
    output = daily_dir / f"{entry_date.isoformat()}.md"

    if output.exists():
        content = output.read_text(encoding="utf-8")
    else:
        template = (root / "editorial" / "daily-template.md").read_text(encoding="utf-8")
        content = template.replace("{{date}}", entry_date.isoformat()).rstrip() + "\n"

    marker = f"- URL: <{url}>"
    if marker in content.splitlines():
        return output, False

    block = [
        "",
        marker,
        _field("タイトル", title),
        _field("種別", kind),
        _field("テーマ", topics),
        _field("要約", summary),
        _field("一言", note),
        _field("Atlas", atlas_path),
        "  - 週刊候補: 検討中",
    ]
    output.write_text(content.rstrip() + "\n" + "\n".join(block) + "\n", encoding="utf-8")
    return output, True


def main() -> int:
    parser = argparse.ArgumentParser(description="週刊GeoAIの日次メモへURLを保存する")
    parser.add_argument("url")
    parser.add_argument("--note", default="", help="公開可能な一言")
    parser.add_argument("--title", default="", help="確認済みのタイトル")
    parser.add_argument("--kind", default="", help="記事、論文、リリースなどの種別")
    parser.add_argument("--topics", default="", help="カンマ区切りのテーマ")
    parser.add_argument("--summary", default="", help="確認済み情報による公開用の短い要約")
    parser.add_argument("--atlas-path", default="", help="対応するAtlasページのリポジトリ相対パス")
    parser.add_argument("--date", type=date.fromisoformat, dest="entry_date")
    args = parser.parse_args()

    try:
        path, created = capture(
            args.url,
            note=args.note,
            title=args.title,
            kind=args.kind,
            topics=args.topics,
            summary=args.summary,
            atlas_path=args.atlas_path,
            entry_date=args.entry_date,
        )
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    action = "保存しました" if created else "既に保存済みです"
    print(f"{action}: {path.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
