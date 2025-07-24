# a_star_example.py
"""
Example demonstrating A* search on a small graph.
"""

from algorithms.graph.a_star import a_star

def heuristic(node, goal):
    # Example heuristic: constant (could be Euclidean or problem-specific)
    return 0

def main():
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    path, cost = a_star(graph, 'A', 'D', heuristic)
    print("A* Path:", path)
    print("A* Cost:", cost)

if __name__ == "__main__":
    main()
