import os

# Base project directory
base_dir = r"E:\git_slow\SoftwareMechatronics"

# Directory structure
dirs = [
    "data_structures",
    "algorithms/search",
    "algorithms/sort",
    "algorithms/graph",
    "algorithms/dp",
    "algorithms/backtracking",
    "algorithms/misc",
    "computation_models",
    "utils",
    "examples",
    "tests",
    "docs/diagrams"
]

# Files to create in each directory
files = {
    "data_structures": ["array.py", "linked_list.py", "stack.py", "queue.py", "hash_table.py", "tree.py", "graph.py", "union_find.py", "__init__.py"],
    "algorithms/search": ["binary_search.py", "bfs_dfs.py", "__init__.py"],
    "algorithms/sort": ["merge_sort.py", "quick_sort.py", "__init__.py"],
    "algorithms/graph": ["dijkstra.py", "prim_kruskal.py", "bellman_ford.py", "__init__.py"],
    "algorithms/dp": ["knapsack.py", "edit_distance.py", "lis.py", "__init__.py"],
    "algorithms/backtracking": ["n_queens.py", "sudoku_solver.py", "__init__.py"],
    "algorithms/misc": ["topological_sort.py", "__init__.py"],
    "computation_models": ["finite_state_machine.py", "pushdown_automaton.py", "turing_machine.py", "lambda_calculus.py", "combinatory_logic.py", "__init__.py"],
    "utils": ["memoization.py", "bitmasking.py", "benchmarks.py", "__init__.py"],
    "examples": ["held_karp_tsp.py", "dijkstra_vs_bellman.py", "fibonacci_comparison.py", "__init__.py"],
    "tests": ["test_data_structures.py", "test_algorithms.py", "test_models.py", "__init__.py"],
    "docs/diagrams": []
}

# Create directories and files
for d in dirs:
    dir_path = os.path.join(base_dir, d)
    os.makedirs(dir_path, exist_ok=True)
    if d in files:
        for file in files[d]:
            file_path = os.path.join(dir_path, file)
            with open(file_path, "w") as f:
                f.write(f"# {file}\n\n# Placeholder for {file} implementation.\n")

# Add a __init__.py in base package
with open(os.path.join(base_dir, "__init__.py"), "w") as f:
    f.write("# Package init\n")

# Add README.md to base
readme_path = os.path.join(base_dir, "README.md")
with open(readme_path, "w") as f:
    f.write("# Software Mechatronics\n\nSee README_basic_machines.md for details.\n")

print(f"Scaffold created at {base_dir}")
