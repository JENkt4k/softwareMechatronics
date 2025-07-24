# test_algorithms.py

import unittest
from algorithms.search.binary_search import binary_search
from algorithms.search.bfs_dfs import bfs, dfs
from algorithms.sort.merge_sort import merge_sort
from algorithms.sort.quick_sort import quick_sort
from algorithms.graph.dijkstra import dijkstra
from algorithms.graph.bellman_ford import bellman_ford
from algorithms.dp.knapsack import knapsack

class TestAlgorithms(unittest.TestCase):

    def test_binary_search(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 3), 2)
        self.assertEqual(binary_search(arr, 6), -1)

    def test_bfs_dfs(self):
        graph = {0: [1, 2], 1: [3], 2: [4], 3: [], 4: []}
        self.assertEqual(bfs(graph, 0), [0, 1, 2, 3, 4])
        self.assertEqual(dfs(graph, 0), [0, 1, 3, 2, 4])

    def test_sorting(self):
        arr = [3, 1, 4, 1, 5]
        self.assertEqual(merge_sort(arr.copy()), [1, 1, 3, 4, 5])
        self.assertEqual(quick_sort(arr.copy()), [1, 1, 3, 4, 5])

    def test_graph_algorithms(self):
        graph = {'A': {'B': 1}, 'B': {'A': 1, 'C': 2}, 'C': {'B': 2}}
        self.assertEqual(dijkstra(graph, 'A')['C'], 3)
        self.assertEqual(bellman_ford(graph, 'A')['C'], 3)

    def test_knapsack(self):
        weights = [1, 3, 4]
        values = [15, 20, 30]
        capacity = 4
        self.assertEqual(knapsack(weights, values, capacity), 35)

if __name__ == '__main__':
    unittest.main()
