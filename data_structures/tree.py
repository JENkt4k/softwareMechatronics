# tree.py
"""
Binary Tree Implementation
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def inorder(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.inorder(node.left, result)
            result.append(node.value)
            self.inorder(node.right, result)
        return result


if __name__ == "__main__":
    bt = BinaryTree(1)
    bt.root.left = TreeNode(2)
    bt.root.right = TreeNode(3)
    print(bt.inorder(bt.root))
