# floyd_warshall_example.py
"""
Example: Floyd-Warshall all-pairs shortest path algorithm.
"""

from algorithms.graph.floyd_warshall import floyd_warshall

def main():
    graph = {
        'A': {'B': 5, 'C': 9},
        'B': {'A': 5, 'C': 2, 'D': 6},
        'C': {'A': 9, 'B': 2, 'D': 3},
        'D': {'B': 6, 'C': 3}
    }
    dist = floyd_warshall(graph)
    print("All-Pairs Shortest Paths:")
    for u in dist:
        print(f"{u}: {dist[u]}")

if __name__ == "__main__":
    main()
