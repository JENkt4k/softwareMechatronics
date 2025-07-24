# topological_sort.py
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
