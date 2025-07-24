# heap_visual_demo.py
"""
Visualization of BinaryHeap using matplotlib.
Displays the heap as a tree structure.
"""

import matplotlib.pyplot as plt
from composites.data_structures.heap import BinaryHeap

def _plot_heap(heap, ax):
    def draw_node(idx, x, y, dx):
        ax.text(x, y, str(heap.tree.get(idx)),
                ha='center', va='center',
                bbox=dict(boxstyle='round', facecolor='lightgreen', edgecolor='black'))
        left = heap.tree.left(idx)
        right = heap.tree.right(idx)
        if left is not None:
            ax.plot([x, x - dx], [y, y - 2], color='black')
            draw_node(left, x - dx, y - 2, dx / 2)
        if right is not None:
            ax.plot([x, x + dx], [y, y - 2], color='black')
            draw_node(right, x + dx, y - 2, dx / 2)

    if len(heap.tree) > 0:
        draw_node(0, 0, 0, 8)

def visualize_heap(heap, title="BinaryHeap"):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title(title)
    ax.axis('off')
    _plot_heap(heap, ax)
    plt.show()

def main():
    heap = BinaryHeap([5, 3, 8, 1, 2], min_heap=True)
    visualize_heap(heap, "Initial Min-Heap")
    heap.push(0)
    visualize_heap(heap, "After pushing 0")
    heap.pop()
    visualize_heap(heap, "After popping root")

if __name__ == "__main__":
    main()