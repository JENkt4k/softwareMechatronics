# test_array_binary_tree.py
"""
Unit tests for ArrayBinaryTree implementation.
"""

import unittest
from data_structures.array_binary_tree import ArrayBinaryTree

class TestArrayBinaryTree(unittest.TestCase):

    def setUp(self):
        self.tree = ArrayBinaryTree([1, 2, 3, 4, 5, 6, 7])

    def test_build_from_list(self):
        self.assertEqual(len(self.tree), 7)
        self.assertEqual(self.tree.get(0), 1)
        self.assertEqual(self.tree.get(6), 7)

    def test_insert(self):
        self.tree.insert(8)
        self.assertEqual(len(self.tree), 8)
        self.assertEqual(self.tree.get(7), 8)

    def test_parent_child(self):
        self.assertEqual(self.tree.parent(4), 1)  # Parent of index 4 is index 1
        self.assertEqual(self.tree.left(1), 3)    # Left child of index 1 is index 3
        self.assertEqual(self.tree.right(1), 4)   # Right child of index 1 is index 4

    def test_get_none(self):
        self.assertIsNone(self.tree.get(100))  # Out of bounds index

    def test_str_representation(self):
        self.assertIn("1, 2, 3", str(self.tree))

if __name__ == '__main__':
    unittest.main()