# SoftwareMechatronics

*A curated collection of fundamental data structures, algorithms, and computational models — the "basic machines" of computing — implemented in Python with examples, tests, and visual diagrams.*

---

## **Features**

### **Data Structures**
- Arrays, Linked Lists, Stacks, Queues
- Hash Tables, Binary Trees, Graphs
- Union-Find (Disjoint Sets)

### **Algorithms**
- **Searching:** Binary Search, BFS, DFS
- **Sorting:** Merge Sort, Quick Sort
- **Graph Algorithms:** Dijkstra, Bellman-Ford, Prim, Kruskal, Topological Sort
- **Dynamic Programming (DP):** Knapsack, Edit Distance, LIS, Held-Karp TSP
- **Backtracking:** N-Queens, Sudoku Solver

### **Computation Models**
- Finite State Machines (FSM)
- Pushdown Automaton (PDA)
- Turing Machines
- Lambda Calculus
- Combinatory Logic (SKI Combinators)

### **Utilities**
- Memoization, Bitmasking helpers
- Benchmarking decorators and tools

---

## **Project Structure**

```
SoftwareMechatronics/
│
├── algorithms/            # Core algorithms
├── data_structures/       # Basic data structures
├── computation_models/    # FSM, Turing, Lambda, etc.
├── utils/                 # Helper utilities
├── examples/              # Example scripts (TSP, Dijkstra vs Bellman-Ford)
├── tests/                 # Unit tests for all modules
└── docs/diagrams/         # Visual diagrams of dependencies
```

---

## **Installation**

Clone the repository and install in **editable mode**:
```bash
git clone https://github.com/yourusername/SoftwareMechatronics.git
cd SoftwareMechatronics
D:/Users/james/AppData/Local/Programs/Python/Python311/python.exe -m pip install -e .
```

---

## **Usage Examples**

### **Run an Example**
```bash
python -m examples.dijkstra_vs_bellman
```

### **Import in Python**
```python
from SoftwareMechatronics.algorithms.graph.dijkstra import dijkstra

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

print(dijkstra(graph, 'A'))
```

---

## **Testing**

Run all unit tests:
```bash
python -m unittest discover tests
```

---

## **Diagrams**
Visual dependency graphs and algorithm/data structure relationships are available in `docs/diagrams/`.

---

## **License**
This project is licensed under the MIT License.
