import tempfile
import unittest
from pathlib import Path

from scripts.check_site_links import Page, check, fragment_problem


class SiteLinksTests(unittest.TestCase):
    def test_inline_text_and_hidden_code(self):
        page = Page('<p>日本<strong>地図</strong>です</p><script>秘密</script><p>次</p>')
        self.assertEqual(page.text, '日本地図です 次')

    def test_encoded_delimiters_and_range_order(self):
        self.assertIsNone(fragment_problem('a,b c&d', 'text=a%2Cb&text=c%26d'))
        self.assertIsNone(fragment_problem('start middle end', 'text=start,end'))
        self.assertIsNotNone(fragment_problem('end start', 'text=start,end'))
        self.assertIsNotNone(fragment_problem('start', 'text=missing'))
        self.assertIsNotNone(fragment_problem('start', 'text=prefix-,start'))

    def test_references_and_history_severity(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            def write(name, body):
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(body, encoding='utf-8')
            write('index.html', '<a href="page/#ok">ok</a><img src="image.svg"><a href="https://other.test/missing">external</a>')
            write('image.svg', '<svg/>')
            write('page/index.html', '<p id="ok">current text</p>')
            write('updates/2026-10-05/index.html', '<a href="https://example.test/project/page/#:~:text=old">old</a>')
            write('updates/2026-10-06/index.html', '<a href="/project/page/#:~:text=current%20text">new</a>')
            errors, warnings, _, count, selected = check(root, 'https://example.test/project/')
            self.assertEqual(errors, [])
            self.assertEqual(len(warnings), 1)
            self.assertEqual((count, selected), (2, '2026-10-06'))
            write('index.html', '<a href="page/#bad">bad</a><img src="missing.svg">')
            write('updates/2026-10-06/index.html', '<a href="/project/page/#:~:text=absent">bad</a>')
            errors, _, _, _, _ = check(root, 'https://example.test/project/')
            self.assertEqual(len(errors), 3)
            with self.assertRaises(ValueError):
                check(root, 'https://example.test/project/', '2026-10-07')

    def test_empty_build_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                check(Path(directory), 'https://example.test/')
