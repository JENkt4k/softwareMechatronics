# a_star.py
"""
A* Algorithm Implementation

This module implements the A* shortest path algorithm for graphs represented
as adjacency dictionaries.
"""

import heapq

def a_star(graph, start, goal, heuristic):
    """
    A* shortest path algorithm.

    :param graph: Dict representation of graph {node: {neighbor: cost}}.
    :param start: Starting node.
    :param goal: Goal node.
    :param heuristic: A function h(n) estimating distance from n to goal.
    :return: (path, total_cost)
    """
    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {node: float("inf") for node in graph}
    g_score[start] = 0

    f_score = {node: float("inf") for node in graph}
    f_score[start] = heuristic(start, goal)

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current), g_score[current]

        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None, float("inf")


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


# Example heuristic (dummy for graph nodes)
def zero_heuristic(node, goal):
    return 0


if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    path, cost = a_star(graph, 'A', 'D', zero_heuristic)
    print("Path:", path, "Cost:", cost)
