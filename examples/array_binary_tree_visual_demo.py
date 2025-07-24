# array_binary_tree_visual_demo.py
"""
Visualization of ArrayBinaryTree using matplotlib.
Displays the tree level by level in a graphical layout.
"""

import matplotlib.pyplot as plt
from data_structures.array_binary_tree import ArrayBinaryTree

def _plot_array_tree(tree, ax):
    def draw_node(idx, x, y, dx):
        ax.text(x, y, str(tree.get(idx)),
                ha='center', va='center',
                bbox=dict(boxstyle='round', facecolor='lightblue', edgecolor='black'))
        left = tree.left(idx)
        right = tree.right(idx)
        if left is not None:
            ax.plot([x, x - dx], [y, y - 2], color='black')
            draw_node(left, x - dx, y - 2, dx / 2)
        if right is not None:
            ax.plot([x, x + dx], [y, y - 2], color='black')
            draw_node(right, x + dx, y - 2, dx / 2)
    if len(tree) > 0:
        draw_node(0, 0, 0, 8)


def visualize_array_tree(tree, title="ArrayBinaryTree"):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title(title)
    ax.axis('off')
    _plot_array_tree(tree, ax)
    plt.show()

def main():
    tree = ArrayBinaryTree([1, 2, 3, 4, 5, 6, 7])
    visualize_array_tree(tree, "Initial Tree")
    tree.insert(8)
    visualize_array_tree(tree, "After inserting 8")
    tree.insert(9)
    visualize_array_tree(tree, "After inserting 9")

if __name__ == "__main__":
    main()