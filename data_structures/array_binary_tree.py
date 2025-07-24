# array_binary_tree.py
"""
Array-Based Binary Tree
-----------------------
A simple array representation of a complete binary tree.
This structure is optimized for memory and cache locality and is the basis
for binary heaps, segment trees, and priority queues.
"""

class ArrayBinaryTree:
    def __init__(self, elements=None):
        """
        Initialize the ArrayBinaryTree with optional elements.
        Elements are stored in level-order starting at index 0.
        """
        self.tree = []
        if elements:
            self.build_from_list(elements)

    def build_from_list(self, elements):
        """Builds a complete binary tree from a list of elements."""
        self.tree = list(elements)

    def insert(self, value):
        """Insert a value into the tree (maintains complete structure)."""
        self.tree.append(value)

    def parent(self, i):
        """Return index of parent of node at index i, or None if root."""
        return (i - 1) // 2 if i > 0 else None

    def left(self, i):
        """Return index of left child of node at index i, or None if out of bounds."""
        left_index = 2 * i + 1
        return left_index if left_index < len(self.tree) else None

    def right(self, i):
        """Return index of right child of node at index i, or None if out of bounds."""
        right_index = 2 * i + 2
        return right_index if right_index < len(self.tree) else None

    def get(self, i):
        """Return value at index i."""
        return self.tree[i] if 0 <= i < len(self.tree) else None

    def __len__(self):
        return len(self.tree)

    def __str__(self):
        return "ArrayBinaryTree(" + ", ".join(map(str, self.tree)) + ")"


if __name__ == "__main__":
    # Demo usage
    elements = [1, 2, 3, 4, 5, 6, 7]
    tree = ArrayBinaryTree(elements)
    print(tree)
    print("Parent of index 4:", tree.parent(4))
    print("Left child of index 1:", tree.left(1))
    print("Right child of index 1:", tree.right(1))
    tree.insert(8)
    print("After insert:", tree)
