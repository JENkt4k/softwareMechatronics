# fortune_voronoi_demo.py
"""
Voronoi Diagram Demo using Fortune's Algorithm (Simplified).
"""

import matplotlib.pyplot as plt
from composites.geometry.fortune_voronoi import fortune_voronoi

def main():
    points = [(100, 100), (300, 100), (200, 300), (400, 400), (100, 400)]
    
    edges = fortune_voronoi(points)
    
    # Plot points
    px, py = zip(*points)
    plt.scatter(px, py, c='black', marker='o', label='Sites')

    # Plot edges
    for start, end in edges:
        if start and end:
            plt.plot([start[0], end[0]], [start[1], end[1]], 'r-')
        elif start:
            plt.plot(start[0], start[1], 'ro')

    plt.title("Voronoi Diagram (Fortune's Algorithm)")
    plt.legend()
    plt.axis('equal')
    plt.show()

if __name__ == "__main__":
    main()
