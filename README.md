# SoftwareMechatronics

An educational Python collection of data structures, algorithms, and computation models, with examples and diagrams. Version 0.1.0 is under development.

## Implemented features

- Data structures: arrays, linked lists, stacks, queues, hash tables, binary trees, array binary trees, AVL trees, graphs, and union-find.
- Searching and sorting: binary search, BFS, DFS, merge sort, and quick sort.
- Graph algorithms: Dijkstra, Bellman-Ford, A*, Floyd-Warshall, Prim, Kruskal, Edmonds-Karp max flow, and topological sort.
- Dynamic programming: knapsack, edit distance, LIS, and a Held-Karp TSP example.
- Backtracking and optimization: N-Queens, Sudoku, and simulated annealing for TSP.
- String matching: KMP.
- Computation models: FSM, PDA, Turing machine, lambda calculus, and SKI combinators.
- Utilities and composites: memoization, bitmask helpers, timing, binary heaps, line sweep, bounded Fortune-sweep Voronoi diagrams, and brute-force raster Voronoi visualization.

Implementation does not imply complete validation. See the limitations below and the [status report](docs/diagrams/audit_reports/audit_report.md).

## Installation

Python 3.8 or newer is declared supported; the cleanup checks were run on Python 3.9.

```bash
git clone https://github.com/JENkt4k/softwareMechatronics.git
cd softwareMechatronics
python -m pip install -e .
```

The core library uses the standard library. Install optional dependencies for plotting and raster Voronoi:

```bash
python -m pip install -e ".[visuals]"
```

For the SciPy comparison demo, use `python -m pip install -e ".[reference]"` instead. These extras also supply NumPy for the expanded benchmark script.

`SoftwareMechatronics` is the distribution name. Python imports use the top-level packages shown below.

## Usage

```python
from algorithms.graph.dijkstra import dijkstra

graph = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "C": 2, "D": 5},
    "C": {"A": 4, "B": 2, "D": 1},
    "D": {"B": 5, "C": 1},
}
print(dijkstra(graph, "A"))
```

Run examples as modules:

```bash
python -m examples.dijkstra_vs_bellman
python -m examples.held_karp_tsp
python -m examples.heap_demo
```

With the visuals extra installed:

```bash
python -m examples.array_binary_tree_visual_demo
python -m examples.heap_visual_demo
python -m composites.geometry.fortune_voronoi_demo
```

The last command visualizes **brute-force** raster Voronoi regions. For computed diagram edges and a sweep animation:

```bash
python -m examples.geometry.fortune_voronoi_demo
python -m examples.geometry.fortune_voronoi_avl_demo
```

The animation retains its historical filename but now uses the linked beachline and processes both site and circle events.

### Bounded Voronoi API

```python
from composites.geometry.fortune_voronoi import fortune_voronoi

edges = fortune_voronoi([(1, 1), (4, 1), (2, 4)], bbox=(0, 0, 5, 5))
# Each edge is ((x1, y1), (x2, y2)).
```

The bounding box is `(xmin, ymin, xmax, ymax)`. Results contain the internal cell boundaries clipped to the box, not its perimeter. Duplicate sites are ignored; zero or one unique site produces no internal edges. Sites outside the box are supported. Invalid/nonfinite coordinates and reversed/zero-area bounds raise `ValueError`.

`FortuneVoronoi.compute()` returns the edges and can be called repeatedly. Its `vertices` attribute contains unique clipped edge endpoints. `step()` exposes individual sweep events in normalized coordinates; use `to_world()` for display. `fortune_voronoi_2` remains a compatibility alias.

The sweep discovers neighboring sites using exact parabola formulas and site/circle events, then clips their bisectors against nearest-site half-planes. A linked beachline and explicit clipping give **O(n^2) worst-case time**, rather than the optimized balanced-tree Fortune algorithm's O(n log n). This is an educational floating-point implementation; features below approximately 1e-12 of the total coordinate span may be lost. Coordinate spans that overflow floating point are rejected. See [implementation notes](docs/fortune_voronoi.md).

## Testing

From the repository root:

```bash
python -m unittest discover -s tests -v
```

All maintained unit tests live directly in `tests/`, including AVL invariants and line-sweep tests. Passing tests cover selected cases, not every algorithm or edge case.

## Known limitations

Known correctness gaps in other modules:

- The PDA's balanced-parentheses example does not reliably recognize balanced input; epsilon transitions and stack/acceptance behavior need review.
- Lambda substitution is not capture-avoiding.
- Line sweep can miss shared-endpoint intersections because end events sort before start events at the same x-coordinate.

These modules should not be treated as fully validated general-purpose implementations.

## Project structure

- `algorithms/`: searching, sorting, graph, DP, backtracking, string, and optimization algorithms.
- `data_structures/`: foundational structures.
- `composites/`: heaps and geometry compositions.
- `computation_models/`: interpreters and automata.
- `utils/`: memoization, bitmasking, and benchmarks.
- `examples/`: runnable demonstrations.
- `tests/`: unit tests, excluded from the installed distribution.
- `docs/diagrams/`: diagrams, benchmark notes, and the status report.

![Array binary tree](docs/diagrams/array_tree.png)
![Binary heap](docs/diagrams/heap.png)

## License

Copyright (c) 2026 James Nelson. Released under the [MIT License](LICENSE).
