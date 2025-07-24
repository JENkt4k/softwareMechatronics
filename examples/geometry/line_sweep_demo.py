# line_sweep_demo.py
"""
Visualization demo for Line Sweep Algorithm using matplotlib.
Shows line segments and intersection points.
"""

import matplotlib.pyplot as plt
from composites.geometry.line_sweep import line_sweep_intersections

def plot_segments(segments, intersections):
    for (x1, y1), (x2, y2) in segments:
        plt.plot([x1, x2], [y1, y2], marker='o')
    for i, j in intersections:
        (p1, q1), (p2, q2) = segments[i], segments[j]
        intersection_point = find_intersection(p1, q1, p2, q2)
        if intersection_point:
            plt.scatter(*intersection_point, color='red', s=50, zorder=5)
    plt.title("Line Sweep Intersection Demo")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()

def find_intersection(p1, q1, p2, q2):
    # Line intersection formula for two line segments
    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]
    xdiff = (p1[0] - q1[0], p2[0] - q2[0])
    ydiff = (p1[1] - q1[1], p2[1] - q2[1])
    div = det(xdiff, ydiff)
    if div == 0:
        return None  # Parallel or coincident
    d = (det(p1, q1), det(p2, q2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

def main():
    segments = [
        ((1, 1), (4, 4)),
        ((1, 4), (4, 1)),
        ((2, 5), (2, 0)),
        ((0, 3), (5, 3))
    ]
    intersections = line_sweep_intersections(segments)
    print("Intersections:", intersections)
    plot_segments(segments, intersections)

if __name__ == "__main__":
    main()
