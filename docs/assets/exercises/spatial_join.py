# /// script
# requires-python = ">=3.11"
# dependencies = ["shapely==2.1.2"]
# ///
"""Synthetic point/polygon exercise. No files, accounts, or network at runtime."""
import json
import platform

import shapely
from shapely import Point, box


def summarize(points, areas, predicate):
    memberships = {
        name: [area for area, shape in areas.items() if predicate(point, shape)]
        for name, point in points.items()
    }
    return {
        "input_points": len(points),
        "memberships": memberships,
        "matched_rows": sum(len(matches) for matches in memberships.values()),
        "matched_unique_points": sum(bool(matches) for matches in memberships.values()),
        "unmatched": [name for name, matches in memberships.items() if not matches],
        "multiple": [name for name, matches in memberships.items() if len(matches) > 1],
        "area_counts": {
            area: sum(area in matches for matches in memberships.values()) for area in areas
        },
    }


def main():
    # Arbitrary Cartesian coordinates; these are not longitude/latitude or real shops.
    areas = {"A": box(0, 0, 10, 10), "B": box(10, 0, 20, 10)}
    points = {
        "P1": Point(5, 5),
        "P2": Point(15, 5),
        "P3": Point(10, 5),  # shared boundary
        "P4": Point(25, 5),  # outside both areas
    }
    results = {
        "within": summarize(points, areas, shapely.within),
        "covered_by": summarize(points, areas, shapely.covered_by),
    }
    expected = {
        "within": {"P1": ["A"], "P2": ["B"], "P3": [], "P4": []},
        "covered_by": {"P1": ["A"], "P2": ["B"], "P3": ["A", "B"], "P4": []},
    }
    for mode, result in results.items():
        if result["memberships"] != expected[mode]:
            raise RuntimeError(f"Unexpected membership result: {mode}")
        if result["matched_unique_points"] + len(result["unmatched"]) != len(points):
            raise RuntimeError(f"Point accounting failed: {mode}")
    print(json.dumps({
        "python": platform.python_version(),
        "shapely": shapely.__version__,
        "geos": shapely.geos_version_string,
        "results": results,
        "check": "PASS",
    }, indent=2))


if __name__ == "__main__":
    main()
