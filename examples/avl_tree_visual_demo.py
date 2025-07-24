#avl_tree_visual_demo2.py
"""
Improved AVL Tree Visualization Demo using matplotlib.
Centers the tree and adjusts spacing dynamically.
"""

import matplotlib.pyplot as plt
from data_structures.avl_tree import AVLTree, AVLNode

def _get_tree_height(node):
    if not node:
        return 0
    return 1 + max(_get_tree_height(node.left), _get_tree_height(node.right))

def _plot_tree(node, x, y, dx, dy, ax):
    if node is None:
        return

    ax.text(x, y, str(node.key), ha='center', va='center',
            bbox=dict(boxstyle='round', facecolor='lightblue', edgecolor='black'))

    if node.left:
        ax.plot([x, x - dx], [y - 0.5, y - dy + 0.5], color='black')
        _plot_tree(node.left, x - dx, y - dy, dx / 2, dy, ax)

    if node.right:
        ax.plot([x, x + dx], [y - 0.5, y - dy + 0.5], color='black')
        _plot_tree(node.right, x + dx, y - dy, dx / 2, dy, ax)

def visualize_tree(tree, title="AVL Tree"):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title(title)
    ax.axis('off')
    if tree.root:
        height = _get_tree_height(tree.root)
        # Start from top center
        _plot_tree(tree.root, x=0, y=0, dx=2 ** (height - 1), dy=2, ax=ax)
        ax.set_xlim(-2 ** height, 2 ** height)
        ax.set_ylim(-2 * height, 2)
    plt.show()

# def main():
#     tree = AVLTree()
#     keys = [10, 20, 30, 40, 50, 25]

#     for key in keys:
#         tree.insert(key)
#         #move visualize_tree into loop to visualize after each insertion
    
#     visualize_tree(tree, title=f"After inserting {key}") #close window will continue

#     for key in [40, 10]:
#         tree.delete(key)
    
#     visualize_tree(tree, title=f"After deleting {key}") #close window will continue


def visualize_update(tree, ax, title="AVL Tree"):
    ax.clear()
    ax.set_title(title)
    ax.axis('off')

    if tree.root:
        height = _get_tree_height(tree.root)
        _plot_tree(tree.root, x=0, y=0, dx=2 ** (height - 1), dy=2, ax=ax)
        ax.set_xlim(-2 ** height, 2 ** height)
        ax.set_ylim(-2 * height, 2)

    plt.draw()
    plt.pause(0.8)  # pause for a moment to visualize

def main():
    plt.ion()
    fig, ax = plt.subplots(figsize=(8, 6))

    tree = AVLTree()
    keys = [10, 20, 30, 40, 50, 25]

    for key in keys:
        tree.insert(key)
        visualize_update(tree, ax, title=f"After inserting {key}")

    for key in [40, 10]:
        tree.delete(key)
        visualize_update(tree, ax, title=f"After deleting {key}")

    plt.ioff()
    plt.show()

if __name__ == "__main__":
    main()