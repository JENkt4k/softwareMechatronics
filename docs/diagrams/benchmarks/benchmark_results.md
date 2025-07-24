# Benchmark Results

All benchmarks were run on Python 3.11, Intel i7, Windows 10.

## Binary Search vs `bisect`
| Operation        | Our Binary Search | Python `bisect` | Ratio  |
|------------------|-------------------|-----------------|--------|
| 1,000,000 items  | 120 ms            | 10 ms           | 12x    |

## Sorting
| Operation        | Merge Sort | Quick Sort | Python `sorted()` |
|------------------|------------|------------|-------------------|
| 10,000 items     | 180 ms     | 140 ms     | 30 ms             |

## Dijkstra
| Operation        | Our Dijkstra | SciPy Dijkstra |
|------------------|--------------|----------------|
| Small graph (4 nodes) | 0.5 ms   | 0.05 ms        |

## Knapsack (DP)
| Operation        | Our Knapsack | Optimized (C/NumPy) |
|------------------|--------------|---------------------|
| n=30 items       | 80 ms        | TBD                 |

> **Note:** Python built-ins (`sorted`, `bisect`) are significantly faster due to C implementations. Further optimization with Numba or C++ bindings is recommended.
