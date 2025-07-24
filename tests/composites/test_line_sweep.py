# test_line_sweep.py
import unittest
from examples.geometry.line_sweep import line_sweep_intersections

class TestLineSweep(unittest.TestCase):
    def test_intersections(self):
        segments = [
            ((1, 1), (4, 4)),
            ((1, 4), (4, 1)),
            ((2, 5), (2, 0)),
            ((0, 3), (5, 3))
        ]
        result = line_sweep_intersections(segments)
        self.assertIn((0, 1), result)
        self.assertIn((2, 3), result)
        self.assertTrue(len(result) >= 2)

if __name__ == "__main__":
    unittest.main()
