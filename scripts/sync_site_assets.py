from __future__ import annotations

import shutil
from pathlib import Path

from common import REPO_ROOT


def sync_logo(root: Path = REPO_ROOT) -> Path:
    source = root / "assets" / "logo.svg"
    destination = root / "docs" / "assets" / "logo.svg"
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)
    return destination


def main() -> int:
    destination = sync_logo()
    print(f"サイト用ロゴを同期しました: {destination.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
