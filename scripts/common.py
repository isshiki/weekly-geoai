from __future__ import annotations

import os
import re
from datetime import date
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFINITION = (
    "本誌では、地図・位置情報・POIなどの地理空間データを、"
    "機械学習やデータサイエンスの手法で分析・活用する領域をGeoAIと呼びます"
)
COMMENTARY_PLACEHOLDERS = (
    "［所感1段落目をここに記入］",
    "［所感2段落目をここに記入］",
)
INTRO_PLACEHOLDER = "［紹介文を1〜2文で記入］"
SUBTITLE_PLACEHOLDER = "［サブタイトルをここに記入］"


def load_dotenv(root: Path = REPO_ROOT) -> dict[str, str]:
    """Load simple KEY=VALUE overrides without an external dependency."""
    values: dict[str, str] = {}
    path = root / ".env"
    if not path.exists():
        return values
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        if key:
            values[key] = value
    return values


def configured_path(name: str, default: str, root: Path = REPO_ROOT) -> Path:
    env_file = load_dotenv(root)
    raw = os.environ.get(name, env_file.get(name, default))
    path = Path(raw)
    return path if path.is_absolute() else root / path


def parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    normalized = text.replace("\r\n", "\n")
    if not normalized.startswith("---\n"):
        raise ValueError("YAML front matter がありません")
    end = normalized.find("\n---\n", 4)
    if end < 0:
        raise ValueError("YAML front matter が閉じられていません")
    metadata: dict[str, str] = {}
    for line in normalized[4:end].splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"front matter の形式が不正です: {line}")
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip("\"")
    return metadata, normalized[end + 5 :].lstrip("\n")


def format_japanese_date(value: date) -> str:
    return f"{value.year}年{value.month}月{value.day}日"


def issue_title(issue_number: int, publication_date: date) -> str:
    return f"週刊GeoAI #{issue_number}（{format_japanese_date(publication_date)}）"


def remove_source_comments(text: str) -> str:
    return re.sub(r"\n?<!-- source-note\b.*?-->\n?", "\n", text, flags=re.DOTALL)
