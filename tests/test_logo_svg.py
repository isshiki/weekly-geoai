from __future__ import annotations

import unittest
import xml.etree.ElementTree as ET
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SVG_NAMESPACE = {"svg": "http://www.w3.org/2000/svg"}


class LogoSvgTest(unittest.TestCase):
    def test_master_logo_has_expected_geometry_and_colors(self) -> None:
        root = ET.parse(REPO_ROOT / "assets" / "logo.svg").getroot()
        self.assertEqual(root.attrib["viewBox"], "0 0 160 160")

        background = root.find("svg:rect", SVG_NAMESPACE)
        self.assertIsNotNone(background)
        assert background is not None
        self.assertEqual(background.attrib["width"], "160")
        self.assertEqual(background.attrib["height"], "160")
        self.assertNotIn("rx", background.attrib)

        fills = {
            element.attrib["fill"]
            for element in root.iter()
            if "fill" in element.attrib
        }
        self.assertEqual(fills, {"#1E3A5F", "#FF8A3D"})
        self.assertIsNone(root.find(".//svg:text", SVG_NAMESPACE))


if __name__ == "__main__":
    unittest.main()
