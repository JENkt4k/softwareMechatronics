# test_a_star.py
import unittest
from algorithms.graph.a_star import a_star, zero_heuristic

class TestAStar(unittest.TestCase):
    def setUp(self):
        self.graph = {
            'A': {'B': 1, 'C': 4},
            'B': {'A': 1, 'C': 2, 'D': 5},
            'C': {'A': 4, 'B': 2, 'D': 1},
            'D': {'B': 5, 'C': 1}
        }

    def test_a_star_path(self):
        path, cost = a_star(self.graph, 'A', 'D', zero_heuristic)
        self.assertEqual(path, ['A', 'B', 'C', 'D'])
        self.assertEqual(cost, 4)

if __name__ == "__main__":
    unittest.main()
