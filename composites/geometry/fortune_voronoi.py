# fortune_voronoi.py
"""
Fortune's Algorithm for Voronoi Diagram Construction (Full Version, Simplified)

This implementation computes Voronoi edges from a set of site points.
It includes both site and circle event handling using a beach line of arcs.

Note: This is a simplified educational version. A robust implementation
would use more sophisticated data structures (e.g., balanced BST for arcs).
"""

import heapq
import math

class Event:
    def __init__(self, y, point, arc=None):
        self.y = y
        self.point = point
        self.arc = arc
        self.valid = True

    def __lt__(self, other):
        return self.y > other.y  # max-heap by y

class Arc:
    def __init__(self, point, prev=None, next=None):
        self.point = point
        self.prev = prev
        self.next = next
        self.event = None
        self.edge_left = None
        self.edge_right = None

class Edge:
    def __init__(self, start, left, right):
        self.start = start
        self.left = left
        self.right = right
        self.end = None

def fortune_voronoi(points):
    """
    Compute a Voronoi diagram for a set of points using Fortune's algorithm.
    :param points: List of (x, y) site coordinates.
    :return: List of Voronoi edges (start, end).
    """
    events = []
    for p in points:
        heapq.heappush(events, Event(p[1], p))

    root = None
    edges = []

    while events:
        event = heapq.heappop(events)
        if event.arc is None:
            root = handle_site_event(event, root, edges, events)
        else:
            if event.valid:
                handle_circle_event(event, root, edges, events)

    return [(edge.start, edge.end) for edge in edges if edge.end]

def handle_site_event(event, root, edges, events):
    p = event.point
    if root is None:
        return Arc(p)

    arc = find_arc_above(p[0], root)
    if arc.event:
        arc.event.valid = False

    new_arc = Arc(p)
    left_arc = Arc(arc.point, arc.prev, new_arc)
    right_arc = Arc(arc.point, new_arc, arc.next)
    new_arc.prev = left_arc
    new_arc.next = right_arc

    if arc.prev:
        arc.prev.next = left_arc
    if arc.next:
        arc.next.prev = right_arc

    if arc == root:
        root = left_arc

    # Create new edge
    new_edge = Edge((p[0], event.y), arc.point, p)
    edges.append(new_edge)
    left_arc.edge_right = new_edge
    new_arc.edge_left = new_edge

    check_circle_event(left_arc, events)
    check_circle_event(right_arc, events)

    return root

def handle_circle_event(event, root, edges, events):
    arc = event.arc
    if arc.prev:
        arc.prev.next = arc.next
        arc.prev.edge_right.end = event.point
    if arc.next:
        arc.next.prev = arc.prev
        arc.next.edge_left.end = event.point

    # Create new edge between arc.prev and arc.next
    new_edge = Edge(event.point, arc.prev.point if arc.prev else None, arc.next.point if arc.next else None)
    edges.append(new_edge)
    if arc.prev:
        arc.prev.edge_right = new_edge
    if arc.next:
        arc.next.edge_left = new_edge

    if arc.prev:
        check_circle_event(arc.prev, events)
    if arc.next:
        check_circle_event(arc.next, events)

def find_arc_above(x, root):
    arc = root
    while arc:
        if arc.next and x > arc.point[0]:
            arc = arc.next
        else:
            return arc
    return arc

def check_circle_event(arc, events):
    if arc.prev is None or arc.next is None:
        return

    a, b, c = arc.prev.point, arc.point, arc.next.point
    if is_counter_clockwise(a, b, c):
        center, radius = circle_center(a, b, c)
        if center:
            y_event = center[1] - radius
            new_event = Event(y_event, (center[0], y_event), arc)
            arc.event = new_event
            heapq.heappush(events, new_event)

def is_counter_clockwise(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]) > 0

def circle_center(a, b, c):
    # Compute the center of the circle passing through a, b, c
    ax, ay = a
    bx, by = b
    cx, cy = c

    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    if d == 0:
        return None, None

    ux = ((ax**2 + ay**2) * (by - cy) + (bx**2 + by**2) * (cy - ay) + (cx**2 + cy**2) * (ay - by)) / d
    uy = ((ax**2 + ay**2) * (cx - bx) + (bx**2 + by**2) * (ax - cx) + (cx**2 + cy**2) * (bx - ax)) / d
    radius = math.sqrt((ux - ax)**2 + (uy - ay)**2)
    return (ux, uy), radius
