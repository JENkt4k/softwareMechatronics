# fortune_voronoi_demo.py
"""
Voronoi Diagram Visualization (Brute Force)

This demo uses brute force Voronoi computation to visualize regions.
"""

import matplotlib.pyplot as plt
import numpy as np
from composites.geometry.voronoi_brute import compute_voronoi_brute

def main():
    points = [(100, 100), (300, 100), (200, 300), (400, 400), (100, 400)]
    width, height = 500, 500
    
    diagram = compute_voronoi_brute(points, width, height)
    plt.imshow(diagram, origin='lower', cmap='tab10', extent=[0, width, 0, height])
    
    # Plot sites
    px, py = zip(*points)
    plt.scatter(px, py, c='black', marker='o')
    plt.title("Brute Force Voronoi Diagram")
    plt.show()

if __name__ == "__main__":
    main()
