from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path

from common import REPO_ROOT


TEXT_SUFFIXES = {".html", ".md", ".py", ".svg", ".toml", ".txt", ".yml", ".yaml"}
IGNORED_DIRECTORIES = {".git", ".venv", "__pycache__", ".pytest_cache"}
PATTERNS = {
    "秘密鍵": re.compile("-----BEGIN " + r"(?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "OpenAI APIキーらしい値": re.compile("sk-" + r"[A-Za-z0-9_-]{20,}"),
    "GitHubトークンらしい値": re.compile("gh" + r"[pousr]_[A-Za-z0-9]{30,}"),
    "AWSアクセスキーらしい値": re.compile("AKIA" + r"[A-Z0-9]{16}"),
}


def _tracked_files(root: Path) -> list[Path]:
    result = subprocess.run(
        ["git", "-c", f"safe.directory={root.resolve()}", "ls-files", "-z"],
        cwd=root,
        check=True,
        capture_output=True,
    )
    return [root / value.decode() for value in result.stdout.split(b"\0") if value]


def _all_files(root: Path) -> list[Path]:
    return [
        path
        for path in root.rglob("*")
        if path.is_file()
        and not IGNORED_DIRECTORIES.intersection(path.relative_to(root).parts)
    ]


def check(*, scan_all: bool = False, root: Path = REPO_ROOT) -> list[str]:
    files = _all_files(root) if scan_all else _tracked_files(root)
    findings: list[str] = []
    for path in files:
        relative = path.relative_to(root)
        if relative.name == ".env" or (
            relative.name.startswith(".env.") and relative.name != ".env.example"
        ):
            findings.append(f"追跡禁止ファイル: {relative}")
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in {".gitignore"}:
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for label, pattern in PATTERNS.items():
            if pattern.search(content):
                findings.append(f"{label}: {relative}")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="公開前に秘密情報らしい内容を検査する")
    parser.add_argument("--all", action="store_true", help="未追跡ファイルを含む全ファイルを検査する")
    args = parser.parse_args()
    try:
        findings = check(scan_all=args.all)
    except (OSError, subprocess.CalledProcessError) as exc:
        parser.error(str(exc))
    if findings:
        print("公開前チェックで問題候補を検出しました:")
        for finding in findings:
            print(f"- {finding}")
        return 1
    print("公開前チェック: 問題候補は見つかりませんでした")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
