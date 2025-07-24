# test_max_flow.py
import unittest
from algorithms.graph.max_flow import edmonds_karp

class TestMaxFlow(unittest.TestCase):
    def setUp(self):
        self.graph = {
            0: {1: 16, 2: 13},
            1: {2: 10, 3: 12},
            2: {1: 4, 4: 14},
            3: {2: 9, 5: 20},
            4: {3: 7, 5: 4},
            5: {}
        }

    def test_max_flow(self):
        max_flow = edmonds_karp(self.graph, 0, 5)
        self.assertEqual(max_flow, 23)

if __name__ == "__main__":
    unittest.main()
