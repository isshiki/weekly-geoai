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
from sync_site_assets import sync_logo  # noqa: E402


class WorkflowTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        shutil.copytree(REPO_ROOT / "editorial", self.root / "editorial")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def test_capture_deduplicates_same_url(self) -> None:
        first_path, first_created = capture(
            "https://example.com/a",
            note="公開できるメモ",
            kind="記事",
            topics="地図, AI",
            summary="確認済みの短い要約である。",
            atlas_path="docs/atlas/methods/example.md",
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
        content = first_path.read_text(encoding="utf-8")
        self.assertEqual(content.count("https://example.com/a"), 1)
        self.assertIn("  - 種別: 記事", content)
        self.assertIn("  - テーマ: 地図, AI", content)
        self.assertIn("  - 要約: 確認済みの短い要約である。", content)
        self.assertIn("  - Atlas: docs/atlas/methods/example.md", content)

    def test_build_rejects_non_friday(self) -> None:
        with self.assertRaisesRegex(ValueError, "金曜日"):
            build(date(2026, 9, 12), issue_number=1, root=self.root)

    def test_build_includes_previous_friday(self) -> None:
        capture(
            "https://example.com/friday",
            title="金曜の記事",
            entry_date=date(2026, 9, 4),
            root=self.root,
        )
        draft = build(date(2026, 9, 11), issue_number=1, root=self.root)
        self.assertIn("https://example.com/friday", draft.read_text(encoding="utf-8"))

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
        self.assertIn("subtitle: ［サブタイトルをここに記入］", content)
        self.assertIn("### 1. [地図AIの事例]", content)
        content = content.replace("［サブタイトルをここに記入］", "地図AIによる更新手法を読む")
        content = content.replace(COMMENTARY_PLACEHOLDERS[0], "今週は地図データの更新手法に動きがあった。")
        content = content.replace(COMMENTARY_PLACEHOLDERS[1], "実務で試す際の入力条件も見ておきたい。")
        content = content.replace(
            INTRO_PLACEHOLDER,
            "地図データをAIで更新する処理手順が公開された。入力データの条件も説明している。",
        )
        draft.write_text(content, encoding="utf-8")

        substack_path = publish(draft, root=self.root)
        substack = substack_path.read_text(encoding="utf-8")
        self.assertIn("週刊GeoAI #1（2026年9月11日）", substack)
        self.assertNotIn("source-note", substack)
        self.assertIn('<a href="https://example.com/map-ai_(demo)">地図AIの事例</a>', substack)
        self.assertFalse((self.root / "docs" / "issues").exists())

    def test_publish_rejects_placeholders(self) -> None:
        capture(
            "https://example.com/a",
            entry_date=date(2026, 9, 7),
            root=self.root,
        )
        draft = build(date(2026, 9, 11), issue_number=1, root=self.root)
        content = draft.read_text(encoding="utf-8")
        content = content.replace("［サブタイトルをここに記入］", "地図AIによる更新手法を読む")
        draft.write_text(content, encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "プレースホルダ"):
            publish(draft, root=self.root)

    def test_sync_site_logo(self) -> None:
        (self.root / "assets").mkdir(parents=True)
        master = self.root / "assets" / "logo.svg"
        master.write_text("<svg>master</svg>\n", encoding="utf-8")

        destination = sync_logo(self.root)

        self.assertEqual(destination, self.root / "docs" / "assets" / "logo.svg")
        self.assertEqual(destination.read_text(encoding="utf-8"), "<svg>master</svg>\n")


if __name__ == "__main__":
    unittest.main()
