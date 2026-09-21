import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from sync_update_history import blocks, review_link, encode


class ReviewLinksTest(unittest.TestCase):
    def test_rendered_text_and_source_exclusion(self):
        self.assertEqual(blocks("---\ntitle: Test\n---\n\n文中の`code`と[リンク](a.md)。\n\n## 出典\n\n除外"), ["文中のcodeとリンク。"])

    def test_only_changed_live_paragraphs(self):
        header = "---\ntitle: テスト\n---\n\n"
        old = header + "変更していない文章をここに置く。\n\n古い本文をここに置いておく。"
        new = header + "変更していない文章をここに置く。\n\n更新した本文をここに置いておく。"
        link = review_link("docs/atlas/tools/test.md", new, old, new, "https://example.com/")
        self.assertIn(encode("更新した本文をここに置いておく。"), link)
        self.assertNotIn(encode("変更していない文章をここに置く。"), link)
        self.assertNotIn(encode("古い本文をここに置いておく。"), link)

    def test_removed_text_is_not_falsely_highlighted(self):
        header = "---\ntitle: テスト\n---\n\n"
        link = review_link("docs/atlas/tools/test.md", header + "後日の書き換え", header, header + "その日に追加した文章である。", "https://example.com")
        self.assertNotIn(":~:", link)
        self.assertIn("ページ全体", link)

    def test_delimiters_are_encoded(self):
        self.assertEqual(encode("a-b,c&d"), "a%2Db%2Cc%26d")


if __name__ == "__main__":
    unittest.main()
