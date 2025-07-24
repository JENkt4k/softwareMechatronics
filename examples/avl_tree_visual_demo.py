# avl_tree_visual_demo.py
"""
AVL Tree Visualization Demo using matplotlib.
Draws the tree structure after each insertion and deletion.
"""

import matplotlib.pyplot as plt
from data_structures.avl_tree import AVLTree, AVLNode

def _plot_tree(node, x=0, y=0, dx=1.0, dy=1.5, ax=None, depth=0):
    if node is None:
        return

    ax.text(x, y, str(node.key), ha='center', va='center',
            bbox=dict(boxstyle='round', facecolor='lightblue', edgecolor='black'))

    # Draw left child
    if node.left:
        ax.plot([x, x - dx], [y - 0.2, y - dy + 0.2], color='black')
        _plot_tree(node.left, x - dx, y - dy, dx / 2, dy, ax, depth + 1)

    # Draw right child
    if node.right:
        ax.plot([x, x + dx], [y - 0.2, y - dy + 0.2], color='black')
        _plot_tree(node.right, x + dx, y - dy, dx / 2, dy, ax, depth + 1)

def visualize_tree(tree, title="AVL Tree"):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title(title)
    ax.axis('off')
    if tree.root:
        _plot_tree(tree.root, x=0, y=0, dx=2.0, dy=1.5, ax=ax)
    plt.show()

def main():
    tree = AVLTree()
    keys = [10, 20, 30, 40, 50, 25]

    for key in keys:
        tree.insert(key)
        visualize_tree(tree, title=f"After inserting {key}")

    for key in [40, 10]:
        tree.delete(key)
        visualize_tree(tree, title=f"After deleting {key}")

if __name__ == "__main__":
    main()