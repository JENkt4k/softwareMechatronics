# bfs_dfs.py
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
