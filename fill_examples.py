import os

examples_dir = r"E:\git_slow\SoftwareMechatronics\examples"

examples_files_content = {
    "held_karp_tsp.py": '''# held_karp_tsp.py
"""
Example: Solving TSP using Held-Karp (DP + Bitmask)
"""

from math import inf

def tsp_held_karp(dist):
    n = len(dist)
    dp = [[inf] * n for _ in range(1 << n)]
    dp[1][0] = 0  # Starting at node 0

    for mask in range(1, 1 << n):
        for u in range(n):
            if not (mask & (1 << u)):
                continue
            for v in range(n):
                if mask & (1 << v):
                    continue
                next_mask = mask | (1 << v)
                dp[next_mask][v] = min(
                    dp[next_mask][v],
                    dp[mask][u] + dist[u][v]
                )

    return min(dp[(1 << n) - 1][v] + dist[v][0] for v in range(1, n))


if __name__ == "__main__":
    dist_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    print(f"Minimum TSP cost: {tsp_held_karp(dist_matrix)}")
''',

    "dijkstra_vs_bellman.py": '''# dijkstra_vs_bellman.py
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
''',

    "fibonacci_comparison.py": '''# fibonacci_comparison.py
"""
Example: Comparing Recursive vs DP Fibonacci
"""

from functools import lru_cache

def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

@lru_cache(maxsize=None)
def fib_dp(n):
    if n <= 1:
        return n
    return fib_dp(n - 1) + fib_dp(n - 2)

if __name__ == "__main__":
    n = 10
    print(f"fib_recursive({n}) = {fib_recursive(n)}")
    print(f"fib_dp({n}) = {fib_dp(n)}")
'''
}

os.makedirs(examples_dir, exist_ok=True)

for filename, content in examples_files_content.items():
    file_path = os.path.join(examples_dir, filename)
    with open(file_path, "w") as f:
        f.write(content)

print(f"Examples created in {examples_dir}")
