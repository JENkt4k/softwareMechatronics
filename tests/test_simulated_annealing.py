# test_simulated_annealing.py
import unittest
import random
from algorithms.optimization.simulated_annealing import solve_tsp

class TestSimulatedAnnealing(unittest.TestCase):
    def test_tsp_example(self):
        distance_matrix = [
            [0, 10, 15, 20],
            [10, 0, 35, 25],
            [15, 35, 0, 30],
            [20, 25, 30, 0]
        ]
        best_route, best_cost = solve_tsp(distance_matrix)
        self.assertEqual(set(best_route), {0, 1, 2, 3})
        self.assertIsInstance(best_cost, (int, float))
        self.assertGreater(best_cost, 0)
        print(f"[INFO] Best Route: {best_route}, Best Cost: {best_cost}")

if __name__ == "__main__":
    unittest.main()
