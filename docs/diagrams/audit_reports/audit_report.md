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
| Geometry | Brute-force raster Voronoi implemented; line sweep has endpoint limitations; bounded Fortune sweep implemented with O(n^2) educational complexity and floating-point precision limits |

## Previous cleanup scope

- Consolidate maintained tests under `tests/` so the documented discovery command includes them.
- Correct Floyd-Warshall's reverse shortest-path expectation (10, via D-C-B-A).
- Align AVL tests with `search(key)` returning the stored value, not a node.
- Correct the line-sweep test import and compare unordered segment pairs.
- Declare explicit package discovery and optional visual/reference dependencies.
- Include string, optimization, and geometry-example packages in distributions; exclude tests.
- Consolidate the Fortune entry points and support the documented bounding-box argument (the subsequent implementation below replaces the sketch).

## Remaining work

1. Fix PDA stack/acceptance and epsilon-transition behavior, capture-avoiding lambda substitution, and line-sweep endpoint handling, with regression tests.
2. Expand coverage of currently untested algorithms and edge cases.
3. Optimize the linked beachline and half-plane clipping if O(n log n) performance is required; consider robust exact predicates for adversarial numerical inputs.
4. Validate across supported Python versions and add CI.

Potential additions such as segment trees, FFT, or parallel algorithms are future ideas, not requirements for the current release. Historical benchmark results are not release-validation evidence.

## Previous cleanup validation

On Python 3.9, all 42 tests passed both from the checkout and against an isolated wheel installation. The wheel built successfully, includes string/optimization/geometry-example packages and optional-dependency metadata, and excludes tests. Six installed console examples ran successfully: Dijkstra/Bellman-Ford, Held-Karp, heap, KMP, A*, and max flow. GUI demos and other Python versions were not validated.

## Fortune implementation and licensing

Added the MIT license with the project author's copyright notice and package license metadata. Replaced approximate beachline logic with parabola intersections, linked arcs, site/circle events, stale-event invalidation, finite edge construction, and bounding-box clipping. Demos now display computed diagrams and an animation of actual sweep events. The legacy import and animation entry point remain available.

The algorithm has O(n^2) worst-case time and floating-point precision limits; these are documented in the README and `docs/fortune_voronoi.md`. It is functional educational geometry, not an exact-predicate or optimized O(n log n) library.

The 57-test suite passes, including analytic diagrams and 120 seeded random/integer diagrams compared with an independent polygon-cell clipping oracle. Additional development checks exercised 1,000 random and 2,000 integer-grid point sets for missing sweep adjacencies.

All ridge adjacencies were also found in 50 seeded SciPy reference diagrams. Both static plot demos and every frame of the sweep animation were rendered with the noninteractive Agg backend.

The package wheel builds successfully. All 57 tests also pass against an isolated wheel installation, and the packaged MIT license matches the repository license byte for byte. Validation used Python 3.9; other Python versions remain unverified.
