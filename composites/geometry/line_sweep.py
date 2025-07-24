# line_sweep.py
"""
Line Sweep Algorithm for Detecting Intersections of Line Segments.

This is a demonstration example showing how to use sorting, active sets, and basic data structures
to implement a line sweep approach.
"""

import bisect

def do_intersect(p1, q1, p2, q2):
    """Check if two line segments (p1,q1) and (p2,q2) intersect."""
    def orientation(a, b, c):
        val = (b[1] - a[1]) * (c[0] - b[0]) - (b[0] - a[0]) * (c[1] - b[1])
        if val == 0:
            return 0  # colinear
        return 1 if val > 0 else 2  # clock or counterclock wise

    def on_segment(a, b, c):
        return (min(a[0], c[0]) <= b[0] <= max(a[0], c[0]) and
                min(a[1], c[1]) <= b[1] <= max(a[1], c[1]))

    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True

    # Special Cases
    if o1 == 0 and on_segment(p1, p2, q1): return True
    if o2 == 0 and on_segment(p1, q2, q1): return True
    if o3 == 0 and on_segment(p2, p1, q2): return True
    if o4 == 0 and on_segment(p2, q1, q2): return True

    return False


def line_sweep_intersections(segments):
    events = []
    for i, (p, q) in enumerate(segments):
        if p[0] > q[0]:
            p, q = q, p  # Ensure left to right
        events.append((p[0], 'start', i))
        events.append((q[0], 'end', i))

    events.sort()
    active = []
    intersections = []

    for x, etype, idx in events:
        if etype == 'start':
            for aidx in active:
                if do_intersect(*segments[aidx], *segments[idx]):
                    intersections.append((aidx, idx))
            bisect.insort(active, idx)
        else:
            if idx in active:  # SAFEGUARD
                active.remove(idx)

    return intersections

if __name__ == "__main__":
    segments = [
        ((1, 1), (4, 4)),
        ((1, 4), (4, 1)),
        ((2, 5), (2, 0)),
        ((0, 3), (5, 3))
    ]
    print("Intersections:", line_sweep_intersections(segments))
