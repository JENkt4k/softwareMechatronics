import os

tests_dir = r"E:\git_slow\SoftwareMechatronics\tests"

tests_files_content = {
    "test_data_structures.py": '''# test_data_structures.py

import unittest
from data_structures.array import Array
from data_structures.linked_list import LinkedList
from data_structures.stack import Stack
from data_structures.queue import Queue
from data_structures.hash_table import HashTable
from data_structures.union_find import UnionFind

class TestDataStructures(unittest.TestCase):

    def test_array(self):
        arr = Array(3)
        arr.set(0, 10)
        self.assertEqual(arr.get(0), 10)
        with self.assertRaises(IndexError):
            arr.get(5)

    def test_linked_list(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        self.assertEqual(ll.display(), [1, 2])

    def test_stack(self):
        s = Stack()
        s.push(10)
        self.assertEqual(s.pop(), 10)
        self.assertTrue(s.is_empty())

    def test_queue(self):
        q = Queue()
        q.enqueue(5)
        q.enqueue(6)
        self.assertEqual(q.dequeue(), 5)
        self.assertEqual(q.dequeue(), 6)
        self.assertTrue(q.is_empty())

    def test_hash_table(self):
        ht = HashTable()
        ht.insert("a", 1)
        self.assertEqual(ht.get("a"), 1)
        ht.delete("a")
        self.assertIsNone(ht.get("a"))

    def test_union_find(self):
        uf = UnionFind(5)
        uf.union(0, 1)
        uf.union(1, 2)
        self.assertEqual(uf.find(0), uf.find(2))

if __name__ == '__main__':
    unittest.main()
''',

    "test_algorithms.py": '''# test_algorithms.py

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
''',

    "test_models.py": '''# test_models.py

import unittest
from computation_models.finite_state_machine import FSM
from computation_models.lambda_calculus import Lambda, evaluate
from computation_models.combinatory_logic import S, K, I

class TestComputationModels(unittest.TestCase):

    def test_fsm(self):
        states = {"q0", "q1"}
        alphabet = {"0", "1"}
        transition = {"q0": {"0": "q0", "1": "q1"}, "q1": {"0": "q0", "1": "q1"}}
        fsm = FSM(states, alphabet, transition, "q0", {"q1"})
        self.assertTrue(fsm.accepts("01"))
        self.assertFalse(fsm.accepts("00"))

    def test_lambda_calculus(self):
        identity = Lambda("x", "x")
        expr = (identity, "y")
        self.assertEqual(evaluate(expr), "y")

    def test_combinatory_logic(self):
        s, k, i = S(), K(), I()
        self.assertEqual(i("Hello"), "Hello")
        self.assertEqual(k("X")("Y"), "X")
        self.assertEqual(s(k)(k)("Z"), "Z")

if __name__ == '__main__':
    unittest.main()
'''
}

os.makedirs(tests_dir, exist_ok=True)

for filename, content in tests_files_content.items():
    file_path = os.path.join(tests_dir, filename)
    with open(file_path, "w") as f:
        f.write(content)

print(f"Tests with sys.path fix created in {tests_dir}")
