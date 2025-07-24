# floyd_warshall.py
"""
Floyd-Warshall Algorithm

Computes the shortest paths between all pairs of nodes in a weighted graph.
"""

import math

def floyd_warshall(graph):
    """
    Floyd-Warshall all-pairs shortest path algorithm.

    :param graph: A dict representation {u: {v: weight}} of a weighted graph.
    :return: distance matrix as a dict of dicts.
    """
    nodes = list(graph.keys())
    dist = {u: {v: math.inf for v in nodes} for u in nodes}
    
    for u in nodes:
        dist[u][u] = 0
        for v, w in graph[u].items():
            dist[u][v] = w

    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


if __name__ == "__main__":
    graph = {
        'A': {'B': 5, 'C': 9},
        'B': {'A': 5, 'C': 2, 'D': 6},
        'C': {'A': 9, 'B': 2, 'D': 3},
        'D': {'B': 6, 'C': 3}
    }
    dist = floyd_warshall(graph)
    for u in dist:
        print(f"{u}: {dist[u]}")
