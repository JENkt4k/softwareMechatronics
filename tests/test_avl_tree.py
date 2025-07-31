import unittest
from data_structures.avl_tree import AVLTree

class TestAVLTree(unittest.TestCase):

    def setUp(self):
        self.tree = AVLTree()
        # Insert key-value pairs
        pairs = [(10, 'A'), (20, 'B'), (5, 'C'), (4, 'D'), (15, 'E')]
        for k, v in pairs:
            self.tree.insert(k, v)

    def test_inorder_keys(self):
        keys = list(self.tree.inorder())
        self.assertEqual(keys, [4, 5, 10, 15, 20])

    def test_inorder_values(self):
        values = self.tree.inorder_values()
        self.assertEqual(values, ['D', 'C', 'A', 'E', 'B'])

    def test_search(self):
        self.assertEqual(self.tree.search(10), 'A')
        self.assertEqual(self.tree.search(15), 'E')
        self.assertIsNone(self.tree.search(99))

if __name__ == '__main__':
    unittest.main()
