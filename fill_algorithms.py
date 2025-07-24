import os

# Adjust this path to your local repo
algorithms_dir = r"E:\git_slow\SoftwareMechatronics\algorithms"

# Content for algorithms/search
search_files_content = {
    "binary_search.py": '''# binary_search.py
"""
Binary Search Implementation
"""

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9]
    print(binary_search(arr, 5))  # Expected: 2
''',

    "bfs_dfs.py": '''# bfs_dfs.py
"""
Breadth-First Search (BFS) and Depth-First Search (DFS) Implementations
"""

from collections import deque

def bfs(graph, start):
    visited, queue = set(), deque([start])
    order = []
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            order.append(vertex)
            queue.extend(graph[vertex])
    return order

def dfs(graph, start, visited=None, order=None):
    if visited is None:
        visited = set()
    if order is None:
        order = []
    visited.add(start)
    order.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, order)
    return order

if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5, 6],
        3: [1],
        4: [1],
        5: [2],
        6: [2]
    }
    print("BFS:", bfs(graph, 0))
    print("DFS:", dfs(graph, 0))
'''
}

# Content for algorithms/sort
sort_files_content = {
    "merge_sort.py": '''# merge_sort.py
"""
Merge Sort Implementation
"""

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print(merge_sort(arr))
''',

    "quick_sort.py": '''# quick_sort.py
"""
Quick Sort Implementation
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    arr = [3, 6, 8, 10, 1, 2, 1]
    print(quick_sort(arr))
'''
}

# Content for algorithms/graph
graph_files_content = {
    "dijkstra.py": '''# dijkstra.py
"""
Dijkstra's Algorithm for Shortest Paths
"""

import heapq

def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    print(dijkstra(graph, 'A'))
''',

    "prim_kruskal.py": '''# prim_kruskal.py
"""
Prim's and Kruskal's Algorithm for Minimum Spanning Tree
"""

def prim(graph, start):
    visited = set([start])
    edges = [
        (weight, start, to)
        for to, weight in graph[start].items()
    ]
    mst = []
    while edges:
        edges.sort()
        weight, frm, to = edges.pop(0)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, weight))
            for next_to, next_weight in graph[to].items():
                if next_to not in visited:
                    edges.append((next_weight, to, next_to))
    return mst

def kruskal(graph):
    edges = []
    for u in graph:
        for v, w in graph[u].items():
            edges.append((w, u, v))
    edges.sort()
    parent = {}
    
    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]
    
    def union(u, v):
        root_u, root_v = find(u), find(v)
        if root_u != root_v:
            parent[root_v] = root_u

    for node in graph:
        parent[node] = node
    mst = []
    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, weight))
    return mst

if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    print("Prim's:", prim(graph, 'A'))
    print("Kruskal's:", kruskal(graph))
''',

    "bellman_ford.py": '''# bellman_ford.py
"""
Bellman-Ford Algorithm for Shortest Paths
"""

def bellman_ford(graph, start):
    distance = {node: float("inf") for node in graph}
    distance[start] = 0

    for _ in range(len(graph) - 1):
        for u in graph:
            for v, w in graph[u].items():
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w

    for u in graph:
        for v, w in graph[u].items():
            if distance[u] + w < distance[v]:
                raise ValueError("Graph contains a negative weight cycle")
    return distance

if __name__ == "__main__":
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'C': 3, 'D': 2, 'E': 3},
        'C': {'B': 1, 'D': 4, 'E': 5},
        'D': {'E': 1},
        'E': {}
    }
    print(bellman_ford(graph, 'A'))
'''
}

# Content for algorithms/misc
misc_files_content = {
    "topological_sort.py": '''# topological_sort.py
"""
Topological Sort for Directed Acyclic Graphs (DAG)
"""

from collections import defaultdict

def topological_sort(vertices, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    visited, stack = set(), []

    def dfs(v):
        visited.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(v)

    for v in vertices:
        if v not in visited:
            dfs(v)
    stack.reverse()
    return stack

if __name__ == "__main__":
    vertices = [5, 4, 2, 3, 1, 0]
    edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
    print(topological_sort(vertices, edges))
'''
}

# Helper to write files
def write_files(base_path, files_content):
    os.makedirs(base_path, exist_ok=True)
    for filename, content in files_content.items():
        with open(os.path.join(base_path, filename), "w") as f:
            f.write(content)

# Write all algorithm categories
write_files(os.path.join(algorithms_dir, "search"), search_files_content)
write_files(os.path.join(algorithms_dir, "sort"), sort_files_content)
write_files(os.path.join(algorithms_dir, "graph"), graph_files_content)
write_files(os.path.join(algorithms_dir, "misc"), misc_files_content)

print(f"All algorithm files have been created in {algorithms_dir}")
