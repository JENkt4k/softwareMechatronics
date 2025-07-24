"""
benchmark_suite.py
Expanded Benchmark and Correctness Suite for SoftwareMechatronics basic machines.
"""

import timeit
import numpy as np
from bisect import bisect_left
from algorithms.search.binary_search import binary_search
from algorithms.sort.merge_sort import merge_sort
from algorithms.sort.quick_sort import quick_sort
from algorithms.graph.dijkstra import dijkstra as our_dijkstra
from algorithms.graph.bellman_ford import bellman_ford as our_bellman_ford
from algorithms.dp.knapsack import knapsack
from algorithms.dp.edit_distance import edit_distance
from algorithms.backtracking.n_queens import solve_n_queens
from algorithms.backtracking.sudoku_solver import solve_sudoku

try:
    import networkx as nx
except ImportError:
    nx = None
    print("[Warning] networkx not installed. Graph benchmarks may be skipped.")

try:
    from scipy.sparse.csgraph import dijkstra as scipy_dijkstra
except ImportError:
    scipy_dijkstra = None
    print("[Warning] scipy not installed. Dijkstra benchmark may be skipped.")


# ===============================
# Correctness Checks
# ===============================

def check_binary_search():
    arr = [1, 2, 3, 4, 5]
    assert binary_search(arr, 1) == 0
    assert binary_search(arr, 5) == 4
    assert binary_search(arr, 6) == -1
    print("[OK] Binary Search correctness.")

def check_sorting():
    arr = [5, 3, 1, 4, 2]
    expected = sorted(arr)
    assert merge_sort(arr) == expected
    assert quick_sort(arr) == expected
    print("[OK] Merge Sort & Quick Sort correctness.")

def check_dijkstra():
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    result = our_dijkstra(graph, 'A')
    assert result['A'] == 0
    assert result['D'] == 4
    print("[OK] Dijkstra correctness.")

def check_knapsack():
    weights = [1, 3, 4]
    values = [15, 20, 30]
    capacity = 4
    assert knapsack(weights, values, capacity) == 35
    print("[OK] Knapsack correctness.")

def check_edit_distance():
    assert edit_distance("kitten", "sitting") == 3
    assert edit_distance("flaw", "lawn") == 2
    print("[OK] Edit Distance correctness.")

def check_n_queens():
    solutions = solve_n_queens(4)
    assert len(solutions) == 2
    print("[OK] N-Queens correctness.")


# ===============================
# Benchmarks
# ===============================

def benchmark_binary_search():
    arr = list(range(1000000))
    target = 999999
    t1 = timeit.timeit(lambda: binary_search(arr, target), number=10000)
    t2 = timeit.timeit(lambda: bisect_left(arr, target), number=10000)
    return ("Binary Search", t1, t2)

def benchmark_sorting():
    arr = np.random.randint(0, 100000, 10000).tolist()
    t1 = timeit.timeit(lambda: merge_sort(arr.copy()), number=10)
    t2 = timeit.timeit(lambda: quick_sort(arr.copy()), number=10)
    t3 = timeit.timeit(lambda: sorted(arr.copy()), number=10)
    return ("Sorting", t1, t2, t3)

def benchmark_dijkstra():
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    nodes = list(graph.keys())
    index = {n: i for i, n in enumerate(nodes)}
    matrix = np.full((len(nodes), len(nodes)), np.inf)
    np.fill_diagonal(matrix, 0)
    for u, edges in graph.items():
        for v, w in edges.items():
            matrix[index[u], index[v]] = w
    t1 = timeit.timeit(lambda: our_dijkstra(graph, 'A'), number=1000)
    t2 = None
    if scipy_dijkstra:
        t2 = timeit.timeit(lambda: scipy_dijkstra(matrix, directed=False), number=1000)
    return ("Dijkstra", t1, t2)

def benchmark_knapsack():
    weights = [1, 3, 4]
    values = [15, 20, 30]
    capacity = 4
    t1 = timeit.timeit(lambda: knapsack(weights, values, capacity), number=10000)
    return ("Knapsack", t1)

def benchmark_edit_distance():
    t1 = timeit.timeit(lambda: edit_distance("kitten", "sitting"), number=5000)
    return ("Edit Distance", t1)


# ===============================
# Runner
# ===============================

def run_correctness():
    print("=== Correctness Checks ===")
    check_binary_search()
    check_sorting()
    check_dijkstra()
    check_knapsack()
    check_edit_distance()
    check_n_queens()
    print("All correctness checks passed.\n")

def run_benchmarks():
    print("=== Benchmark Results ===")
    results = []
    results.append(benchmark_binary_search())
    results.append(benchmark_sorting())
    results.append(benchmark_dijkstra())
    results.append(benchmark_knapsack())
    results.append(benchmark_edit_distance())
    for res in results:
        print(res)
    print("\nBenchmarks complete.")

if __name__ == "__main__":
    run_correctness()
    run_benchmarks()
