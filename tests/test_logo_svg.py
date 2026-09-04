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

        self.assertIsNone(root.find("svg:rect", SVG_NAMESPACE))

        pin = root.find("svg:path", SVG_NAMESPACE)
        self.assertIsNotNone(pin)
        assert pin is not None
        self.assertEqual(pin.attrib["fill"], "#FF8A3D")
        self.assertEqual(pin.attrib["stroke"], "#1E3A5F")
        self.assertEqual(pin.attrib["stroke-width"], "6")
        self.assertEqual(pin.attrib["paint-order"], "stroke fill")

        fills = {
            element.attrib["fill"]
            for element in root.iter()
            if "fill" in element.attrib
        }
        self.assertEqual(fills, {"#1E3A5F", "#FF8A3D"})
        self.assertIsNone(root.find(".//svg:text", SVG_NAMESPACE))


if __name__ == "__main__":
    unittest.main()
