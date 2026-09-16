"""Linked beachline and parabola intersections for a downward Fortune sweep.

A linked sequence makes arc splitting/removal explicit. Lookup is O(n); this
educational implementation does not claim the balanced-tree O(log n) bound.
Coordinates are normalized by FortuneVoronoi before reaching this module.
"""

import math


def breakpoint(left, right, sweep_y):
    """Return the x boundary between consecutive left and right site arcs."""
    if left == right:
        return left[0]
    dl, dr = left[1] - sweep_y, right[1] - sweep_y
    if dl == dr:
        return (left[0] + right[0]) / 2
    if dl <= 0:
        return left[0]
    if dr <= 0:
        return right[0]

    # Solve in coordinates relative to the left focus to avoid cancellation
    # from large absolute coordinates. Choose the root for the ordered arcs.
    dx = right[0] - left[0]
    a = (dr - dl) / (2 * dl * dr)
    b = dx / dr
    c = -dx * dx / (2 * dr) + (left[1] - right[1]) / 2
    discriminant = max(0.0, b * b - 4 * a * c)
    q = -0.5 * (b + math.copysign(math.sqrt(discriminant), b))
    if q == 0:
        roots = (-b / (2 * a),) * 2
    else:
        roots = (q / a, c / q)
    offset = min(roots) if left[1] > right[1] else max(roots)
    return left[0] + offset


class ArcNode:
    """One live arc; a site can appear in multiple arcs after a split."""

    def __init__(self, site):
        self.site = site
        self.prev = None
        self.next = None
        self.circle_event = None
        self.alive = True


class BeachLine:
    def __init__(self):
        self.head = None

    def __iter__(self):
        arc = self.head
        while arc is not None:
            yield arc
            arc = arc.next

    def find_arc_above(self, x, sweep_y):
        arc = self.head
        while arc is not None and arc.next is not None:
            if x <= breakpoint(arc.site, arc.next.site, sweep_y):
                break
            arc = arc.next
        return arc

    def append(self, site):
        """Append a site at the initial, equal-height sweep level."""
        new = ArcNode(site)
        if self.head is None:
            self.head = new
        else:
            tail = self.head
            while tail.next is not None:
                tail = tail.next
            tail.next, new.prev = new, tail
        return new

    def split(self, arc, site):
        """Replace arc with old/new/old and return the three live arcs."""
        middle, right = ArcNode(site), ArcNode(arc.site)
        right.next = arc.next
        if right.next is not None:
            right.next.prev = right
        arc.next, middle.prev = middle, arc
        middle.next, right.prev = right, middle
        return arc, middle, right

    def remove(self, arc):
        if arc.prev is None:
            self.head = arc.next
        else:
            arc.prev.next = arc.next
        if arc.next is not None:
            arc.next.prev = arc.prev
        arc.alive = False
