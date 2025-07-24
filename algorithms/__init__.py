"""
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
