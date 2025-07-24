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

DEBUG = True  # Set to False to disable debug output

class Event:
    def __init__(self, y, point, arc=None):
        self.y = y
        self.point = point
        self.arc = arc
        self.valid = True

    def __lt__(self, other):
        return self.y > other.y

    def __repr__(self):
        etype = "Site" if self.arc is None else "Circle"
        return f"<{etype}Event y={self.y:.2f} point={self.point} valid={self.valid}>"

class Arc:
    def __init__(self, point, prev=None, next=None):
        self.point = point
        self.prev = prev
        self.next = next
        self.event = None
        self.edge_left = None
        self.edge_right = None

    def __repr__(self):
        return f"Arc({self.point})"

class Edge:
    def __init__(self, start, left, right):
        self.start = start
        self.left = left
        self.right = right
        self.end = None

    def __repr__(self):
        return f"Edge(start={self.start}, end={self.end}, left={self.left}, right={self.right})"

def fortune_voronoi(points, bbox=(0, 500, 0, 500)):
    events = []
    for p in points:
        heapq.heappush(events, Event(p[1], p))

    root = None
    edges = []

    while events:
        event = heapq.heappop(events)
        if DEBUG:
            print("Processing event:", event)
        if event.arc is None:
            root = handle_site_event(event, root, edges, events)
        else:
            if event.valid:
                handle_circle_event(event, root, edges, events)

        if DEBUG:
            print("Current edges:", edges)

    # Clip edges to bounding box
    return clip_edges(edges, bbox)

def handle_site_event(event, root, edges, events):
    p = event.point
    if DEBUG:
        print(f"Site event at {p}")
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

    midpoint = ((p[0] + arc.point[0]) / 2, event.y)
    new_edge = Edge(midpoint, arc.point, p)
    edges.append(new_edge)

    left_arc.edge_right = new_edge
    new_arc.edge_left = new_edge
    new_arc.edge_right = new_edge
    right_arc.edge_left = new_edge

    check_circle_event(left_arc, events)
    check_circle_event(right_arc, events)

    return root

def handle_circle_event(event, root, edges, events):
    arc = event.arc
    if DEBUG:
        print(f"Circle event at {event.point} removing arc {arc}")

    if arc.prev and arc.prev.edge_right:
        arc.prev.edge_right.end = event.point
    if arc.next and arc.next.edge_left:
        arc.next.edge_left.end = event.point

    if arc.prev:
        arc.prev.next = arc.next
    if arc.next:
        arc.next.prev = arc.prev

    if arc.prev and arc.next:
        new_edge = Edge(event.point, arc.prev.point, arc.next.point)
        edges.append(new_edge)
        arc.prev.edge_right = new_edge
        arc.next.edge_left = new_edge

        check_circle_event(arc.prev, events)
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
            if DEBUG:
                print(f"  Added circle event at y={y_event:.2f} center={center}")

def is_counter_clockwise(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]) > 0

def circle_center(a, b, c):
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

def clip_edges(edges, bbox):
    xmin, xmax, ymin, ymax = bbox
    clipped_edges = []
    for e in edges:
        start, end = e.start, e.end
        if start and end:
            sx, sy = max(xmin, min(xmax, start[0])), max(ymin, min(ymax, start[1]))
            ex, ey = max(xmin, min(xmax, end[0])), max(ymin, min(ymax, end[1]))
            clipped_edges.append(((sx, sy), (ex, ey)))
    return clipped_edges