# array_binary_tree_demo.py
"""
Demo for ArrayBinaryTree.
Displays the tree as level-order lists after each operation.
"""

from data_structures.array_binary_tree import ArrayBinaryTree

def print_tree_levels(tree):
    """Prints the tree in level-by-level format."""
    n = len(tree)
    level = 0
    i = 0
    while i < n:
        level_size = 2 ** level
        nodes = [str(tree.get(j)) if j < n else "-" for j in range(i, min(i + level_size, n))]
        print("Level", level, ":", " ".join(nodes))
        i += level_size
        level += 1
    print("-" * 40)

def main():
    elements = [1, 2, 3, 4, 5, 6, 7]
    tree = ArrayBinaryTree(elements)
    print("Initial tree:")
    print_tree_levels(tree)

    # Insert a new value
    for value in [8, 9]:
        print(f"Inserting {value}...")
        tree.insert(value)
        print_tree_levels(tree)

    # Access parents and children
        idx = 4
    parent_idx = tree.parent(idx)
    print(f"Parent of index {idx} ({tree.get(idx)}):",
          tree.get(parent_idx) if parent_idx is not None else None)

    left_idx = tree.left(idx)
    right_idx = tree.right(idx)
    print(f"Left child of index {idx}:",
          tree.get(left_idx) if left_idx is not None else None)
    print(f"Right child of index {idx}:",
          tree.get(right_idx) if right_idx is not None else None)


if __name__ == "__main__":
    main()
