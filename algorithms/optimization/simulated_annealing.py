# simulated_annealing.py
"""
Simulated Annealing Algorithm

This implementation provides a generic simulated annealing framework, 
as well as an example for solving the Traveling Salesman Problem (TSP).
"""

import math
import random

def simulated_annealing(initial_solution, cost_function, neighbor_function,
                        initial_temp=1000, cooling_rate=0.995, min_temp=1e-3, max_iter=10000):
    """
    Perform simulated annealing optimization.

    :param initial_solution: The starting solution.
    :param cost_function: A function that evaluates the cost of a solution.
    :param neighbor_function: A function that generates a neighboring solution.
    :param initial_temp: The initial temperature.
    :param cooling_rate: The rate at which the temperature decreases.
    :param min_temp: The stopping temperature.
    :param max_iter: Maximum number of iterations.
    :return: The best solution found and its cost.
    """
    current_solution = initial_solution
    current_cost = cost_function(current_solution)
    best_solution = current_solution
    best_cost = current_cost
    temp = initial_temp

    for _ in range(max_iter):
        if temp < min_temp:
            break
        neighbor = neighbor_function(current_solution)
        neighbor_cost = cost_function(neighbor)
        cost_diff = neighbor_cost - current_cost
        if cost_diff < 0 or random.random() < math.exp(-cost_diff / temp):
            current_solution, current_cost = neighbor, neighbor_cost
            if current_cost < best_cost:
                best_solution, best_cost = current_solution, current_cost
        temp *= cooling_rate

    return best_solution, best_cost


# Example: TSP Problem
def tsp_cost(route, distance_matrix):
    return sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1)) + distance_matrix[route[-1]][route[0]]


def tsp_neighbor(route):
    a, b = random.sample(range(len(route)), 2)
    new_route = route[:]
    new_route[a:b] = reversed(new_route[a:b])
    return new_route


def solve_tsp(distance_matrix):
    initial_route = list(range(len(distance_matrix)))
    random.shuffle(initial_route)
    best_route, best_cost = simulated_annealing(
        initial_route,
        lambda r: tsp_cost(r, distance_matrix),
        tsp_neighbor,
        initial_temp=1000,
        cooling_rate=0.999,
        max_iter=10000
    )
    return best_route, best_cost


if __name__ == "__main__":
    # Example usage
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    best_route, best_cost = solve_tsp(distance_matrix)
    print("Best Route:", best_route)
    print("Best Cost:", best_cost)
