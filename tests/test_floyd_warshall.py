# test_floyd_warshall.py
import unittest
from algorithms.graph.floyd_warshall import floyd_warshall

class TestFloydWarshall(unittest.TestCase):
    def setUp(self):
        self.graph = {
            'A': {'B': 5, 'C': 9},
            'B': {'A': 5, 'C': 2, 'D': 6},
            'C': {'A': 9, 'B': 2, 'D': 3},
            'D': {'B': 6, 'C': 3}
        }

    def test_all_pairs_shortest_paths(self):
        dist = floyd_warshall(self.graph)
        self.assertEqual(dist['A']['D'], 10)  # A->B->D = 5 + 6 = 11; A->C->D = 9 + 3 = 12, but A->B->C->D = 5 + 2 + 3 = 10
        self.assertEqual(dist['B']['C'], 2)
        self.assertEqual(dist['C']['B'], 2)
        self.assertEqual(dist['D']['A'], 11)

if __name__ == "__main__":
    unittest.main()
