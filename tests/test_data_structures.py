# test_data_structures.py
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
