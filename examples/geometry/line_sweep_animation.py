# line_sweep_animation.py
"""
Line Sweep Animation Demo

Visualizes the line sweep algorithm for segment intersections using matplotlib's animation.
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

# Precompute all intersection events
events = []
for i, (p, q) in enumerate(segments):
    if p[0] > q[0]:
        p, q = q, p
    events.append((p[0], 'start', i))
    events.append((q[0], 'end', i))
events.sort()

# Store intersections as the sweep progresses
intersections = []
active = []

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(0, 6)
ax.set_ylim(0, 6)
ax.set_title("Line Sweep Animation")
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
    global active, intersections
    if frame >= len(events):
        return sweep_line, intersection_dots

    x, etype, idx = events[frame]
    sweep_line.set_xdata([x, x])  # Move sweep line

    if etype == 'start':
        for aidx in active:
            if do_intersect(*segments[aidx], *segments[idx]):
                point = get_intersection_point(segments[aidx], segments[idx])
                if point:
                    intersections.append(point)
        active.append(idx)
    elif etype == 'end':
        if idx in active:
            active.remove(idx)

    # Update intersection dots
    if intersections:
        xs, ys = zip(*intersections)
        intersection_dots.set_data(xs, ys)
    else:
        intersection_dots.set_data([], [])

    return sweep_line, intersection_dots


def get_intersection_point(seg1, seg2):
    # Simple line intersection formula
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

ani = animation.FuncAnimation(fig, update, frames=len(events)+5, interval=1000, blit=False, repeat=False)

plt.legend()
plt.grid(True)
plt.show()
