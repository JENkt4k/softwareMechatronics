# test_avl_tree.py
"""
Unit tests for AVLTree implementation.
"""

import unittest
from data_structures.avl_tree import AVLTree

class TestAVLTree(unittest.TestCase):

    def setUp(self):
        self.tree = AVLTree()
        for key in [10, 20, 30, 40, 50, 25]:
            self.tree.insert(key)

    def test_insertion(self):
        expected_inorder = [10, 20, 25, 30, 40, 50]
        self.assertEqual(self.tree.inorder(), expected_inorder)

    def test_deletion(self):
        self.tree.delete(40)
        expected_inorder = [10, 20, 25, 30, 50]
        self.assertEqual(self.tree.inorder(), expected_inorder)

    def test_search_found(self):
        node = self.tree.search(25)
        self.assertIsNotNone(node)
        self.assertEqual(node.key, 25)

    def test_search_not_found(self):
        node = self.tree.search(99)
        self.assertIsNone(node)

    def test_balance_property(self):
        def check_balance(node):
            if node is None:
                return True
            lh = self.tree._get_height(node.left)
            rh = self.tree._get_height(node.right)
            return abs(lh - rh) <= 1 and check_balance(node.left) and check_balance(node.right)

        self.assertTrue(check_balance(self.tree.root))

if __name__ == '__main__':
    unittest.main()
