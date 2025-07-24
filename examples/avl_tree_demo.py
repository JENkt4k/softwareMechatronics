# avl_tree_demo.py
"""
Interactive AVL Tree demo script.
Prints tree structure (inorder and height) after each operation.
"""

from data_structures.avl_tree import AVLTree

def print_tree(tree):
    print("Inorder traversal:", tree.inorder())
    if tree.root:
        print("Tree height:", tree.root.height)
    print("-" * 40)

def main():
    tree = AVLTree()
    keys = [10, 20, 30, 40, 50, 25]
    print("=== AVL Tree Insertions ===")
    for key in keys:
        print(f"Inserting {key}...")
        tree.insert(key)
        print_tree(tree)

    print("=== AVL Tree Deletions ===")
    for key in [40, 10]:
        print(f"Deleting {key}...")
        tree.delete(key)
        print_tree(tree)

    print("=== Search Test ===")
    search_key = 25
    node = tree.search(search_key)
    print(f"Search for {search_key}:", "Found" if node else "Not Found")

if __name__ == "__main__":
    main()