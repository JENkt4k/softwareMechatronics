# graph.py
"""
Graph Representation (Adjacency List)
"""

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = []

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj_list[u].append(v)

    def get_neighbors(self, v):
        return self.adj_list.get(v, [])


if __name__ == "__main__":
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    print(g.adj_list)
