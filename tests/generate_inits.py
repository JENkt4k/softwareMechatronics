import os

base_dir = r"E:\git_slow\SoftwareMechatronics"

# Content for __init__.py files
root_init = '''"""
Software Mechatronics Package
Core data structures, algorithms, and computation models.
"""

__version__ = "0.1.0"
__author__ = "Your Name or Organization"

from . import algorithms
from . import data_structures
from . import computation_models
from . import utils
'''

algorithms_init = '''"""
Algorithms module: Search, Sort, Graph, DP, Backtracking, Misc.
"""

from .search.binary_search import binary_search
from .search.bfs_dfs import bfs, dfs

from .sort.merge_sort import merge_sort
from .sort.quick_sort import quick_sort

from .graph.dijkstra import dijkstra
from .graph.bellman_ford import bellman_ford
from .graph.prim_kruskal import prim, kruskal

from .dp.knapsack import knapsack
from .dp.edit_distance import edit_distance
from .dp.lis import lis

from .backtracking.n_queens import solve_n_queens
from .backtracking.sudoku_solver import solve_sudoku

from .misc.topological_sort import topological_sort
'''

data_structures_init = '''"""
Core data structures: Array, LinkedList, Stack, Queue, HashTable, Tree, Graph, Union-Find.
"""

from .array import Array
from .linked_list import LinkedList
from .stack import Stack
from .queue import Queue
from .hash_table import HashTable
from .tree import BinaryTree, TreeNode
from .graph import Graph
from .union_find import UnionFind
'''

computation_models_init = '''"""
Computation models: FSM, PDA, Turing Machine, Lambda Calculus, Combinatory Logic.
"""

from .finite_state_machine import FSM
from .pushdown_automaton import PDA
from .turing_machine import TuringMachine
from .lambda_calculus import Lambda, evaluate
from .combinatory_logic import S, K, I
'''

utils_init = '''"""
Utility functions: memoization, bitmasking, and benchmarking.
"""

from .memoization import memoize
from .bitmasking import is_set, set_bit, clear_bit, toggle_bit
from .benchmarks import timeit, benchmark
'''

# Helper to write __init__.py
def write_init(path, content):
    os.makedirs(path, exist_ok=True)
    init_file = os.path.join(path, "__init__.py")
    with open(init_file, "w") as f:
        f.write(content)
    print(f"Updated {init_file}")

# Create __init__.py files
write_init(base_dir, root_init)
write_init(os.path.join(base_dir, "algorithms"), algorithms_init)
write_init(os.path.join(base_dir, "data_structures"), data_structures_init)
write_init(os.path.join(base_dir, "computation_models"), computation_models_init)
write_init(os.path.join(base_dir, "utils"), utils_init)
