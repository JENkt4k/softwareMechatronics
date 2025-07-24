# held_karp_tsp.py
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
