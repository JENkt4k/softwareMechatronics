# Project status audit

Updated September 16, 2026. This is an implementation inventory, not a claim of exhaustive correctness or test coverage.

| Area | Current status |
| --- | --- |
| Search and sorting | Binary search, BFS, DFS, merge sort, quick sort implemented |
| Graph algorithms | Dijkstra, Bellman-Ford, Prim, Kruskal, A*, Floyd-Warshall, Edmonds-Karp, topological sort implemented |
| Dynamic programming | Knapsack, edit distance, LIS implemented; Held-Karp TSP in examples |
| Backtracking | N-Queens and Sudoku implemented |
| Strings and optimization | KMP and simulated-annealing TSP implemented |
| Data structures | Arrays, linked lists, stacks, queues, hash tables, trees, AVL trees, graphs, union-find, and composite heap implemented |
| Computation models | FSM, PDA, Turing machine, lambda calculus, SKI implemented; PDA and lambda correctness gaps remain |
| Geometry | Brute-force raster Voronoi implemented; line sweep has endpoint limitations; Fortune implementation is experimental and unfinished |

## Cleanup scope

- Consolidate maintained tests under `tests/` so the documented discovery command includes them.
- Correct Floyd-Warshall's reverse shortest-path expectation (10, via D-C-B-A).
- Align AVL tests with `search(key)` returning the stored value, not a node.
- Correct the line-sweep test import and compare unordered segment pairs.
- Declare explicit package discovery and optional visual/reference dependencies.
- Include string, optimization, and geometry-example packages in distributions; exclude tests.
- Use a single Fortune sketch, label its demos experimental, and support the documented bounding-box argument.

## Remaining work

1. Fix PDA stack/acceptance and epsilon-transition behavior, capture-avoiding lambda substitution, and line-sweep endpoint handling, with regression tests.
2. Expand coverage of currently untested algorithms and edge cases.
3. Complete Fortune circle events, exact breakpoints, edge construction, and clipping before claiming Voronoi support from that implementation.
4. Validate across supported Python versions and add CI.
5. Resolve licensing: the previous README claimed MIT, but no license file is present.

Potential additions such as segment trees, FFT, or parallel algorithms are future ideas, not requirements for the current release. Historical benchmark results are not release-validation evidence.

## Cleanup validation

On Python 3.9, all 42 tests passed both from the checkout and against an isolated wheel installation. The wheel built successfully, includes string/optimization/geometry-example packages and optional-dependency metadata, and excludes tests. Six installed console examples ran successfully: Dijkstra/Bellman-Ford, Held-Karp, heap, KMP, A*, and max flow. GUI demos and other Python versions were not validated.
