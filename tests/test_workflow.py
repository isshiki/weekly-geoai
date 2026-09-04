from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from build_weekly import build  # noqa: E402
from capture_daily import capture  # noqa: E402
from common import COMMENTARY_PLACEHOLDERS, INTRO_PLACEHOLDER  # noqa: E402
from publish_issue import publish  # noqa: E402


class WorkflowTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        shutil.copytree(REPO_ROOT / "editorial", self.root / "editorial")
        (self.root / "docs" / "issues").mkdir(parents=True)
        shutil.copy2(REPO_ROOT / "docs" / "issues" / "index.md", self.root / "docs" / "issues")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def test_capture_deduplicates_same_url(self) -> None:
        first_path, first_created = capture(
            "https://example.com/a",
            note="公開できるメモ",
            entry_date=date(2026, 9, 7),
            root=self.root,
        )
        second_path, second_created = capture(
            "https://example.com/a",
            entry_date=date(2026, 9, 7),
            root=self.root,
        )
        self.assertEqual(first_path, second_path)
        self.assertTrue(first_created)
        self.assertFalse(second_created)
        self.assertEqual(first_path.read_text(encoding="utf-8").count("https://example.com/a"), 1)

    def test_build_rejects_non_friday(self) -> None:
        with self.assertRaisesRegex(ValueError, "金曜日"):
            build(date(2026, 9, 12), issue_number=1, root=self.root)

    def test_build_and_publish_issue(self) -> None:
        capture(
            "https://example.com/map-ai_(demo)",
            title="地図AIの事例",
            note="処理手順を確認したい",
            entry_date=date(2026, 9, 7),
            root=self.root,
        )
        draft = build(date(2026, 9, 11), issue_number=1, root=self.root)
        content = draft.read_text(encoding="utf-8")
        content = content.replace(COMMENTARY_PLACEHOLDERS[0], "今週は地図データの更新手法に動きがあった。")
        content = content.replace(COMMENTARY_PLACEHOLDERS[1], "実務で試す際の入力条件も見ておきたい。")
        content = content.replace(
            INTRO_PLACEHOLDER,
            "地図データをAIで更新する処理手順が公開された。入力データの条件も説明している。",
        )
        draft.write_text(content, encoding="utf-8")

        public_path, substack_path = publish(draft, root=self.root)
        public = public_path.read_text(encoding="utf-8")
        substack = substack_path.read_text(encoding="utf-8")
        self.assertIn("週刊GeoAI #1（2026年9月11日）", public)
        self.assertNotIn("source-note", public)
        self.assertIn('<a href="https://example.com/map-ai_(demo)">地図AIの事例</a>', substack)
        archive = (self.root / "docs" / "issues" / "index.md").read_text(encoding="utf-8")
        self.assertIn("./2026-09-11.html", archive)

    def test_publish_rejects_placeholders(self) -> None:
        capture(
            "https://example.com/a",
            entry_date=date(2026, 9, 7),
            root=self.root,
        )
        draft = build(date(2026, 9, 11), issue_number=1, root=self.root)
        with self.assertRaisesRegex(ValueError, "プレースホルダ"):
            publish(draft, root=self.root)


if __name__ == "__main__":
    unittest.main()
