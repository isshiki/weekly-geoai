import unittest
from scripts.build_atlas_review_register import source_dates


class ReviewRegisterTests(unittest.TestCase):
    def test_only_explicit_source_checks(self):
        source = '''---
updated: 2026-10-06
---
本文は2026-10-05確認。
## 出典
- A（2026-04-22公開、2026-09-02確認）
- B（2026-10-01再確認）
## 次に読む
2026-10-06確認
'''
        self.assertEqual(source_dates(source), ['2026-09-02', '2026-10-01'])

    def test_missing_source_date_is_not_edit_date(self):
        self.assertEqual(source_dates('updated: 2026-10-06\n## 出典\n未確認'), [])
