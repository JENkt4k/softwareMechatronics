# heap.py
"""
Binary Heap Implementation
--------------------------
A binary heap (min-heap or max-heap) built on top of ArrayBinaryTree.
"""

from data_structures.array_binary_tree import ArrayBinaryTree

class BinaryHeap:
    def __init__(self, elements=None, min_heap=True):
        self.min_heap = min_heap
        self.tree = ArrayBinaryTree()
        if elements:
            self.heapify(elements)

    def _compare(self, a, b):
        return a < b if self.min_heap else a > b

    def push(self, value):
        self.tree.insert(value)
        self._sift_up(len(self.tree) - 1)

    def pop(self):
        if len(self.tree) == 0:
            return None
        root = self.tree.tree[0]
        last = self.tree.tree.pop()
        if len(self.tree) > 0:
            self.tree.tree[0] = last
            self._sift_down(0)
        return root

    def peek(self):
        return self.tree.get(0) if len(self.tree) > 0 else None

    def heapify(self, elements):
        self.tree.build_from_list(elements)
        for i in reversed(range(len(self.tree) // 2)):
            self._sift_down(i)

    def _sift_up(self, index):
        parent = self.tree.parent(index)
        while parent is not None and self._compare(self.tree.tree[index], self.tree.tree[parent]):
            self.tree.tree[index], self.tree.tree[parent] = self.tree.tree[parent], self.tree.tree[index]
            index = parent
            parent = self.tree.parent(index)

    def _sift_down(self, index):
        n = len(self.tree)
        while True:
            left = self.tree.left(index)
            right = self.tree.right(index)
            smallest_or_largest = index

            if left is not None and self._compare(self.tree.tree[left], self.tree.tree[smallest_or_largest]):
                smallest_or_largest = left
            if right is not None and self._compare(self.tree.tree[right], self.tree.tree[smallest_or_largest]):
                smallest_or_largest = right

            if smallest_or_largest == index:
                break

            self.tree.tree[index], self.tree.tree[smallest_or_largest] = self.tree.tree[smallest_or_largest], self.tree.tree[index]
            index = smallest_or_largest

    def __len__(self):
        return len(self.tree)

    def __str__(self):
        return "BinaryHeap(" + ", ".join(map(str, self.tree.tree)) + ")"