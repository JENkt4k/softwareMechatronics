# prim_kruskal.py
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
