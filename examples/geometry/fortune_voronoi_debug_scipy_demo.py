# fortune_voronoi_demo.py
"""
Voronoi Diagram Demo with SciPy Comparison.

Displays both the Fortune's algorithm result (our implementation) and
a reference Voronoi diagram from SciPy for comparison.
"""

import matplotlib.pyplot as plt
from composites.geometry.fortune_voronoi import fortune_voronoi

# SciPy reference
from scipy.spatial import Voronoi, voronoi_plot_2d

def main():
    points = [(100, 100), (300, 100), (200, 300), (400, 400), (100, 400)]
    
    # Our Fortune's algorithm edges
    edges = fortune_voronoi(points, bbox=(0, 500, 0, 500))
    
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))
    
    # Plot our implementation
    axs[0].set_title("Fortune's Algorithm (Our Implementation)")
    px, py = zip(*points)
    axs[0].scatter(px, py, c='black', marker='o', label='Sites')
    for start, end in edges:
        if start and end:
            axs[0].plot([start[0], end[0]], [start[1], end[1]], 'r-')
    axs[0].legend()
    axs[0].set_xlim(0, 500)
    axs[0].set_ylim(0, 500)
    axs[0].set_aspect('equal', adjustable='box')
    
    # Plot SciPy reference
    axs[1].set_title("SciPy Voronoi Reference")
    vor = Voronoi(points)
    voronoi_plot_2d(vor, ax=axs[1], show_points=True, show_vertices=False, line_colors='blue')
    axs[1].scatter(px, py, c='black', marker='o')
    axs[1].set_xlim(0, 500)
    axs[1].set_ylim(0, 500)
    axs[1].set_aspect('equal', adjustable='box')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
