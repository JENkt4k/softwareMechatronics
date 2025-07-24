# max_flow_example.py
"""
Example demonstrating Edmonds-Karp (Max Flow) algorithm.
"""

from algorithms.graph.max_flow import edmonds_karp

def main():
    graph = {
        0: {1: 16, 2: 13},
        1: {2: 10, 3: 12},
        2: {1: 4, 4: 14},
        3: {2: 9, 5: 20},
        4: {3: 7, 5: 4},
        5: {}
    }
    max_flow = edmonds_karp(graph, 0, 5)
    print("Max Flow from 0 to 5:", max_flow)

if __name__ == "__main__":
    main()
