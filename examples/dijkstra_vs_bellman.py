# dijkstra_vs_bellman.py
"""
Example: Comparing Dijkstra and Bellman-Ford Algorithms
"""

from algorithms.graph.dijkstra import dijkstra
from algorithms.graph.bellman_ford import bellman_ford

if __name__ == "__main__":
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'C': 3, 'D': 2, 'E': 3},
        'C': {'B': 1, 'D': 4, 'E': 5},
        'D': {'E': 1},
        'E': {}
    }

    print("Dijkstra (from A):", dijkstra(graph, 'A'))
    print("Bellman-Ford (from A):", bellman_ford(graph, 'A'))
