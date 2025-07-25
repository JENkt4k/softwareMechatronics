import os
import matplotlib.pyplot as plt

# Local path for diagrams
images_dir = r"E:\git_slow\SoftwareMechatronics\docs\diagrams"
os.makedirs(images_dir, exist_ok=True)
array_tree_img = os.path.join(images_dir, "array_tree.png")
heap_img = os.path.join(images_dir, "heap.png")

# Minimal ArrayBinaryTree
class ArrayBinaryTree:
    def __init__(self, elements=None):
        self.tree = elements[:] if elements else []

    def __len__(self):
        return len(self.tree)

    def get(self, i):
        return self.tree[i] if 0 <= i < len(self.tree) else None

    def left(self, i):
        li = 2 * i + 1
        return li if li < len(self.tree) else None

    def right(self, i):
        ri = 2 * i + 2
        return ri if ri < len(self.tree) else None


# Minimal BinaryHeap
class BinaryHeap:
    def __init__(self, elements=None, min_heap=True):
        self.tree = ArrayBinaryTree(elements or [])
        self.min_heap = min_heap


# Visualization for ArrayBinaryTree
def plot_array_binary_tree(tree, title, save_path):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title(title)
    ax.axis('off')

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

    plt.savefig(save_path)
    plt.close(fig)


# Visualization for BinaryHeap
def plot_binary_heap(heap, title, save_path):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title(title)
    ax.axis('off')

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

    plt.savefig(save_path)
    plt.close(fig)


# Generate images
tree = ArrayBinaryTree([1, 2, 3, 4, 5, 6, 7, 8, 9])
plot_array_binary_tree(tree, "ArrayBinaryTree Example", array_tree_img)

heap = BinaryHeap([5, 3, 8, 1, 2], min_heap=True)
plot_binary_heap(heap, "BinaryHeap Example", heap_img)

print(f"Saved: {array_tree_img}")
print(f"Saved: {heap_img}")
