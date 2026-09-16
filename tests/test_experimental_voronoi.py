"""Compatibility and status checks for the unfinished Fortune sketch."""
import unittest
from contextlib import redirect_stdout
from io import StringIO

from composites.geometry.fortune_voronoi import FortuneVoronoi, fortune_voronoi
from composites.geometry.fortune_voronoi_2 import FortuneVoronoi as LegacyFortuneVoronoi


class TestExperimentalVoronoi(unittest.TestCase):
    def test_legacy_module_uses_canonical_class(self):
        self.assertIs(LegacyFortuneVoronoi, FortuneVoronoi)

    def test_constructor_warns_and_preserves_bbox(self):
        bbox = (-10, -20, 100, 200)
        with self.assertWarnsRegex(RuntimeWarning, "experimental and incomplete"):
            algorithm = FortuneVoronoi([], bbox=bbox)
        self.assertEqual(algorithm.bbox, bbox)

    def test_wrapper_accepts_bbox_and_warns(self):
        with redirect_stdout(StringIO()):
            with self.assertWarnsRegex(RuntimeWarning, "no Voronoi edges"):
                fortune_voronoi([(100, 400), (300, 300)], bbox=(0, 0, 500, 500))
