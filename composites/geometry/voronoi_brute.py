# voronoi_brute.py
"""
Brute Force Voronoi Diagram Implementation

This module computes a Voronoi diagram by brute force:
- For each pixel in a grid, determine the nearest site point.
- Assign a region color based on nearest site.

This is not efficient (O(n * width * height)) but is useful for visualization
and verifying Fortune's algorithm results later.
"""

import numpy as np

def compute_voronoi_brute(points, width=500, height=500):
    """
    Compute a Voronoi diagram using brute force distance checks.
    
    :param points: List of (x, y) coordinates for sites.
    :param width: Width of the grid.
    :param height: Height of the grid.
    :return: 2D numpy array with index of nearest point for each pixel.
    """
    diagram = np.zeros((height, width), dtype=int)
    points = np.array(points)
    
    # Precompute squared points for efficiency
    for y in range(height):
        for x in range(width):
            distances = np.sum((points - np.array([x, y]))**2, axis=1)
            diagram[y, x] = np.argmin(distances)
    return diagram
