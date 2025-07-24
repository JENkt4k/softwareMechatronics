# bellman_ford.py
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
