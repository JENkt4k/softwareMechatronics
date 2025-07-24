import os

# Path to your data_structures directory
ds_dir = r"E:\git_slow\SoftwareMechatronics\data_structures"

data_structures_files = {
    "array.py": '''# array.py
"""
Simple Array Wrapper
"""

class Array:
    def __init__(self, size):
        self.data = [None] * size
        self.size = size

    def set(self, index, value):
        if 0 <= index < self.size:
            self.data[index] = value
        else:
            raise IndexError("Array index out of bounds")

    def get(self, index):
        if 0 <= index < self.size:
            return self.data[index]
        else:
            raise IndexError("Array index out of bounds")

    def __repr__(self):
        return str(self.data)


if __name__ == "__main__":
    arr = Array(5)
    arr.set(0, 10)
    print(arr.get(0))
    print(arr)
''',

    "linked_list.py": '''# linked_list.py
"""
Singly Linked List
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        elems = []
        while current:
            elems.append(current.value)
            current = current.next
        return elems


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    print(ll.display())
''',

    "stack.py": '''# stack.py
"""
Stack (LIFO)
"""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if self.stack else None

    def peek(self):
        return self.stack[-1] if self.stack else None

    def is_empty(self):
        return len(self.stack) == 0


if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    print(s.pop())  # 20
''',

    "queue.py": '''# queue.py
"""
Queue (FIFO)
"""

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.popleft() if self.queue else None

    def is_empty(self):
        return len(self.queue) == 0


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())  # 1
''',

    "hash_table.py": '''# hash_table.py
"""
Hash Table Implementation
"""

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        idx = self._hash(key)
        for pair in self.table[idx]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[idx].append([key, value])

    def get(self, key):
        idx = self._hash(key)
        for k, v in self.table[idx]:
            if k == key:
                return v
        return None

    def delete(self, key):
        idx = self._hash(key)
        self.table[idx] = [pair for pair in self.table[idx] if pair[0] != key]


if __name__ == "__main__":
    ht = HashTable()
    ht.insert("a", 1)
    print(ht.get("a"))
''',

    "tree.py": '''# tree.py
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
''',

    "graph.py": '''# graph.py
"""
Graph Representation (Adjacency List)
"""

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = []

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj_list[u].append(v)

    def get_neighbors(self, v):
        return self.adj_list.get(v, [])


if __name__ == "__main__":
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    print(g.adj_list)
''',

    "union_find.py": '''# union_find.py
"""
Union-Find (Disjoint Set Union)
"""

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1


if __name__ == "__main__":
    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(1, 2)
    print(uf.find(2))
'''
}

# Ensure directory exists
os.makedirs(ds_dir, exist_ok=True)

# Write files
for filename, content in data_structures_files.items():
    file_path = os.path.join(ds_dir, filename)
    with open(file_path, "w") as f:
        f.write(content)

print(f"Data structure files created in {ds_dir}")
