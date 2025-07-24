import graphviz
import os

# Update to your local path
output_dir = r"E:\git_slow\SoftwareMechatronics\docs\diagrams"
os.makedirs(output_dir, exist_ok=True)

# Create the dependency graph
dot = graphviz.Digraph(comment='Algorithms to Data Structures', format='png')
dot.attr(rankdir='LR')

# Data structures
dot.attr('node', shape='box', style='filled', color='lightblue')
data_structures = ["Array", "Queue", "Stack", "Graph", "Priority Queue", "Union-Find", "2D Array", "Bitmask"]
for ds in data_structures:
    dot.node(ds)

# Algorithms
dot.attr('node', shape='ellipse', style='filled', color='lightyellow')
algorithms = [
    "Binary Search", "Merge Sort", "Quick Sort", "BFS", "DFS", "Dijkstra",
    "Prim", "Kruskal", "Bellman-Ford", "Topological Sort", "Knapsack",
    "Edit Distance", "LIS", "N-Queens", "Sudoku", "TSP (Held-Karp)"
]
for alg in algorithms:
    dot.node(alg)

# Add edges
edges = [
    ("Binary Search", "Array"),
    ("Merge Sort", "Array"),
    ("Quick Sort", "Array"),
    ("BFS", "Graph"),
    ("BFS", "Queue"),
    ("DFS", "Graph"),
    ("DFS", "Stack"),
    ("Dijkstra", "Graph"),
    ("Dijkstra", "Priority Queue"),
    ("Prim", "Graph"),
    ("Prim", "Priority Queue"),
    ("Kruskal", "Graph"),
    ("Kruskal", "Union-Find"),
    ("Bellman-Ford", "Graph"),
    ("Bellman-Ford", "Array"),
    ("Topological Sort", "Graph"),
    ("Topological Sort", "Stack"),
    ("Knapsack", "Array"),
    ("Edit Distance", "2D Array"),
    ("LIS", "Array"),
    ("LIS", "Binary Search"),
    ("N-Queens", "Array"),
    ("Sudoku", "2D Array"),
    ("TSP (Held-Karp)", "2D Array"),
    ("TSP (Held-Karp)", "Bitmask"),
]
for edge in edges:
    dot.edge(*edge)

# Render the PNG in your project path
output_path = os.path.join(output_dir, "dependency_graph")
dot.render(output_path, cleanup=True)

print(f"Dependency graph generated: {output_path}.png")
