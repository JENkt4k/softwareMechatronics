"""Voronoi tests against independent polygon clipping and analytic diagrams."""
import itertools
import math
import random
import unittest

from composites.geometry.beachline import breakpoint
from composites.geometry.fortune_voronoi import FortuneVoronoi, fortune_voronoi
from composites.geometry.fortune_voronoi_2 import FortuneVoronoi as LegacyFortuneVoronoi


def canonical(edges, digits=7):
    return {tuple(sorted(tuple(round(v, digits) for v in p) for p in edge)) for edge in edges}


def reference_edges(points, bbox):
    """Independent O(n^3) oracle: clip every cell polygon, then select ridges.

    No sweep, candidate pairs, or implementation geometry helpers are used.
    Test data is moderate in scale to keep this simple oracle well conditioned.
    """
    xmin, ymin, xmax, ymax = bbox
    points = sorted(set(points))
    edges = []
    for px, py in points:
        cell = [(xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax)]
        for qx, qy in points:
            if (px, py) == (qx, qy):
                continue
            nx, ny = qx - px, qy - py
            limit = (qx*qx + qy*qy - px*px - py*py) / 2
            clipped = []
            for a, b in zip(cell, cell[1:] + cell[:1]):
                da = nx*a[0] + ny*a[1] - limit
                db = nx*b[0] + ny*b[1] - limit
                if da <= 0:
                    clipped.append(a)
                if (da <= 0) != (db <= 0):
                    t = da / (da - db)
                    clipped.append((a[0] + t*(b[0]-a[0]), a[1] + t*(b[1]-a[1])))
            cell = clipped
        for a, b in zip(cell, cell[1:] + cell[:1]):
            if math.hypot(a[0]-b[0], a[1]-b[1]) < 1e-8:
                continue
            # A cell edge is internal exactly when both endpoints lie on a
            # second site's bisector (a box side alone does not qualify).
            for qx, qy in points:
                if (qx, qy) == (px, py):
                    continue
                def residual(p):
                    return ((p[0]-px)**2 + (p[1]-py)**2
                            - (p[0]-qx)**2 - (p[1]-qy)**2)
                if abs(residual(a)) < 1e-7 and abs(residual(b)) < 1e-7:
                    edges.append((a, b))
                    break
    return edges


class TestFortuneVoronoi(unittest.TestCase):
    def assert_reference(self, points, bbox=(-3, -3, 3, 3)):
        actual = fortune_voronoi(points, bbox)
        self.assertEqual(canonical(actual), canonical(reference_edges(points, bbox)))
        self.assertEqual(len(actual), len(canonical(actual)))
        for a, b in actual:
            self.assertGreater(math.hypot(a[0]-b[0], a[1]-b[1]), 0)
            for t in (0, .25, .5, .75, 1):
                p = (a[0] + t*(b[0]-a[0]), a[1] + t*(b[1]-a[1]))
                self.assertGreaterEqual(p[0], bbox[0] - 1e-9)
                self.assertLessEqual(p[0], bbox[2] + 1e-9)
                self.assertGreaterEqual(p[1], bbox[1] - 1e-9)
                self.assertLessEqual(p[1], bbox[3] + 1e-9)
                distances = sorted((p[0]-q[0])**2 + (p[1]-q[1])**2 for q in set(points))
                self.assertAlmostEqual(distances[0], distances[1], places=7)

    def test_empty_single_and_duplicates(self):
        for points in ([], [(1, 2)], [(1, 2)]*4):
            self.assertEqual(fortune_voronoi(points), [])
        self.assertEqual(fortune_voronoi([(0, 0), (2, 0)]*3),
                         fortune_voronoi([(0, 0), (2, 0)]))

    def test_two_sites_analytic(self):
        bbox = (-2, -2, 2, 2)
        self.assertEqual(fortune_voronoi([(-1, 0), (1, 0)], bbox), [((0., -2.), (0., 2.))])
        self.assertEqual(fortune_voronoi([(0, -1), (0, 1)], bbox), [((-2., 0.), (2., 0.))])
        self.assertEqual(fortune_voronoi([(-1, -1), (1, 1)], bbox), [((-2., 2.), (2., -2.))])

    def test_triangle(self):
        self.assert_reference([(-1, 0), (1, 0), (0, 2)])
        algo = FortuneVoronoi([(-1, 0), (1, 0), (0, 2)], (-3, -3, 3, 3))
        self.assertEqual(len(algo.compute()), 3)
        self.assertEqual(algo.circle_events, 1)

    def test_cocircular_square(self):
        points = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        self.assert_reference(points)
        algo = FortuneVoronoi(points, (-3, -3, 3, 3))
        self.assertEqual(len(algo.compute()), 4)
        self.assertEqual(len(algo.vertices), 5)

    def test_cocircular_and_tied_circle_site_events(self):
        for n in (4, 8, 12):
            self.assert_reference([(math.cos(2*math.pi*i/n), math.sin(2*math.pi*i/n)) for i in range(n)])
        self.assert_reference([(-1, 0), (0, 1), (1, 0), (0, -1), (0, 0)])

    def test_collinear(self):
        for points in ([(x, 0) for x in range(-2, 3)],
                       [(0, y) for y in range(-2, 3)],
                       [(x, 2*x) for x in range(-2, 3)]):
            self.assert_reference(points)
            self.assertEqual(len(fortune_voronoi(points, (-10, -10, 10, 10))), 4)

    def test_grid(self):
        self.assert_reference([(x, y) for x in range(-2, 3) for y in range(-2, 3)])

    def test_outside_sites_and_clipping(self):
        self.assert_reference([(-10, 0), (10, 0), (0, 10)], (-1, -1, 1, 1))
        self.assertEqual(fortune_voronoi([(10, 0), (20, 0)], (-1, -1, 1, 1)), [])
        # A bisector touching only a box corner is not a finite edge.
        self.assertEqual(fortune_voronoi([(0, 0), (2, 2)], (0, 0, 1, 1)), [])
        self.assert_reference([(-1, 0), (1, 0)], (0, -1, 1, 1))

    def test_random_diagrams_against_cell_oracle(self):
        for seed in range(80):
            rng = random.Random(seed)
            points = [(rng.uniform(-5, 5), rng.uniform(-5, 5)) for _ in range(20)]
            with self.subTest(seed=seed):
                self.assert_reference(points)

    def test_integer_diagrams_against_cell_oracle(self):
        for seed in range(40):
            rng = random.Random(seed)
            points = [(rng.randrange(-5, 6), rng.randrange(-5, 6)) for _ in range(25)]
            with self.subTest(seed=seed):
                self.assert_reference(points)

    def test_nearly_collinear_sites(self):
        self.assert_reference([(-2, 0), (-1, 1e-8), (0, -1e-8), (1, 2e-8), (2, 0)])

    def test_permutation_invariance(self):
        points = [(0, 1), (-1, 0), (1, 0), (0, -1), (0, 0)]
        expected = fortune_voronoi(points, (-2, -2, 2, 2))
        for permutation in itertools.permutations(points):
            self.assertEqual(fortune_voronoi(permutation, (-2, -2, 2, 2)), expected)

    def test_translation_and_scale(self):
        points = [(-1, 1), (1, 1), (-1, -1), (1, -1), (0, .25)]
        bbox = (-2, -2, 2, 2)
        expected = canonical(fortune_voronoi(points, bbox), 5)
        for scale, offset in ((1e-8, 0), (1e8, 0), (1, 1e8)):
            convert = lambda p: tuple(v*scale + offset for v in p)
            edges = fortune_voronoi([convert(p) for p in points], tuple(v*scale + offset for v in bbox))
            restored = [tuple(tuple((v-offset)/scale for v in p) for p in edge) for edge in edges]
            self.assertEqual(canonical(restored, 5), expected)

    def test_step_circle_events_and_repeatability(self):
        algo = FortuneVoronoi([(-1, 0), (1, 0), (0, 2), (.2, .1)], (-3, -3, 3, 3))
        levels = []
        while True:
            event = algo.step()
            if event is None:
                break
            levels.append(event.y)
            self.assertTrue(event.site_event or event.arc.alive is False)
            arcs = list(algo.beachline)
            for left, right in zip(arcs, arcs[1:]):
                self.assertIs(left.next, right)
                self.assertIs(right.prev, left)
        self.assertEqual(levels, sorted(levels, reverse=True))
        self.assertEqual(algo.site_events, 4)
        self.assertGreater(algo.circle_events, 0)
        first = algo.compute()
        self.assertEqual(first, algo.compute())
        first.clear()
        self.assertTrue(algo.compute())
        self.assertIsNone(algo.step())

    def test_invalid_inputs(self):
        for bbox in [(0, 0, 0, 1), (0, 2, 1, 1), (0, 0, math.inf, 1), (0, 1), None]:
            with self.subTest(bbox=bbox), self.assertRaises(ValueError):
                fortune_voronoi([], bbox)
        for point in [(math.nan, 0), (0, math.inf), (1,), (1, 2, 3), None, ('bad', 0)]:
            with self.subTest(point=point), self.assertRaises(ValueError):
                fortune_voronoi([point])

    def test_legacy_alias(self):
        self.assertIs(LegacyFortuneVoronoi, FortuneVoronoi)


class TestBreakpoints(unittest.TestCase):
    def test_equal_height_and_directrix(self):
        self.assertEqual(breakpoint((-1, 2), (1, 2), 0), 0)
        self.assertEqual(breakpoint((-1, 2), (1, 0), 0), 1)
        self.assertEqual(breakpoint((-1, 0), (1, 2), 0), -1)

    def test_intersection_satisfies_both_parabolas(self):
        for left, right in [((0, 2), (1, 1)), ((1, 1), (0, 2)), ((-2, 3), (1, 2))]:
            x = breakpoint(left, right, 0)
            heights = [(x-p[0])**2 / (2*p[1]) + p[1]/2 for p in (left, right)]
            self.assertAlmostEqual(*heights)
