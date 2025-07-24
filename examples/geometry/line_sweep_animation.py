# line_sweep_animation.py
"""
Improved Line Sweep Animation Demo

Intersections appear exactly when the sweep line crosses their x-coordinate.
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from composites.geometry.line_sweep import do_intersect

# Define segments
segments = [
    ((1, 1), (4, 4)),
    ((1, 4), (4, 1)),
    ((2, 5), (2, 0)),
    ((0, 3), (5, 3))
]

# Precompute all intersection points
def get_intersection_point(seg1, seg2):
    (x1, y1), (x2, y2) = seg1
    (x3, y3), (x4, y4) = seg2

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    xdiff = (x1 - x2, x3 - x4)
    ydiff = (y1 - y2, y3 - y4)
    div = det(xdiff, ydiff)
    if div == 0:
        return None

    d = (det((x1, y1), (x2, y2)), det((x3, y3), (x4, y4)))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return (x, y)

# Gather all intersections
intersections_all = []
for i in range(len(segments)):
    for j in range(i+1, len(segments)):
        if do_intersect(*segments[i], *segments[j]):
            point = get_intersection_point(segments[i], segments[j])
            if point:
                intersections_all.append(point)

# Sort intersections by x-coordinate
intersections_all.sort(key=lambda p: p[0])

# Setup plot
fig, ax = plt.subplots()
ax.set_xlim(0, 6)
ax.set_ylim(0, 6)
ax.set_title("Line Sweep Animation (Improved)")
ax.set_xlabel("X")
ax.set_ylabel("Y")

# Draw all segments
for (x1, y1), (x2, y2) in segments:
    ax.plot([x1, x2], [y1, y2], color='gray', linestyle='--')

# Sweep line (vertical)
sweep_line = ax.axvline(x=0, color='blue', linewidth=1.5, label='Sweep Line')

# Intersection points
intersection_dots, = ax.plot([], [], 'ro', markersize=5, label='Intersections')

def update(frame):
    x_pos = frame / 10.0  # Move sweep line from 0 to ~6
    sweep_line.set_xdata([x_pos, x_pos])

    # Show intersections up to current sweep line x
    visible_points = [p for p in intersections_all if p[0] <= x_pos]
    if visible_points:
        xs, ys = zip(*visible_points)
        intersection_dots.set_data(xs, ys)
    else:
        intersection_dots.set_data([], [])

    return sweep_line, intersection_dots

ani = animation.FuncAnimation(fig, update, frames=int(6*10)+1, interval=200, blit=False, repeat=False)

plt.legend()
plt.grid(True)
plt.show()
