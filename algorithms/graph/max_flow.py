# max_flow.py
"""
Edmonds-Karp Algorithm for Max Flow

This implementation computes the maximum flow from a source to a sink in a directed graph.
"""

from collections import deque

def bfs(residual_graph, source, sink, parent):
    visited = set()
    queue = deque([source])
    visited.add(source)

    while queue:
        u = queue.popleft()
        for v, capacity in residual_graph[u].items():
            if v not in visited and capacity > 0:
                queue.append(v)
                visited.add(v)
                parent[v] = u
                if v == sink:
                    return True
    return False


def edmonds_karp(graph, source, sink):
    """
    Compute maximum flow using Edmonds-Karp algorithm.
    :param graph: Dict representation {u: {v: capacity}}.
    :param source: Source node.
    :param sink: Sink node.
    :return: Maximum flow value.
    """
    # Create residual graph
    residual_graph = {u: dict(v) for u, v in graph.items()}
    for u in graph:
        for v in graph[u]:
            if v not in residual_graph:
                residual_graph[v] = {}
            if u not in residual_graph[v]:
                residual_graph[v][u] = 0

    max_flow = 0
    parent = {}

    while bfs(residual_graph, source, sink, parent):
        # Find the bottleneck capacity
        path_flow = float("inf")
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, residual_graph[u][v])
            v = u

        # Update residual capacities
        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = u

        max_flow += path_flow
        parent = {}

    return max_flow


if __name__ == "__main__":
    graph = {
        0: {1: 16, 2: 13},
        1: {2: 10, 3: 12},
        2: {1: 4, 4: 14},
        3: {2: 9, 5: 20},
        4: {3: 7, 5: 4},
        5: {}
    }
    print("Max Flow:", edmonds_karp(graph, 0, 5))
