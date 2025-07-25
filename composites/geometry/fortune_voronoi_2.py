# fortune_voronoi.py
"""
AVL-based Fortune's Algorithm (skeleton).
Currently handles:
- Site events.
- BeachLine management with AVL tree.
"""

import heapq
from beachline import BeachLine
# from beachline import BeachLine

class Event:
    def __init__(self, y, point, site_event=True):
        self.y = y
        self.point = point
        self.site_event = site_event
        self.valid = True

    def __lt__(self, other):
        return self.y > other.y  # Max-heap behavior for sweep line

    def __repr__(self):
        return f"{'Site' if self.site_event else 'Circle'}Event(y={self.y}, point={self.point})"


class FortuneVoronoi:
    def __init__(self, points, bbox=(0, 0, 500, 500)):
        self.points = sorted(points, key=lambda p: -p[1])  # Sort by y descending
        self.bbox = bbox
        self.events = []
        self.beachline = BeachLine()
        self.edges = []
        self.vertices = []

        for p in self.points:
            heapq.heappush(self.events, Event(p[1], p, site_event=True))

    def process_events(self):
        while self.events:
            event = heapq.heappop(self.events)
            if event.site_event:
                self.handle_site_event(event)
            else:
                self.handle_circle_event(event)

    def handle_site_event(self, event):
        print(f"Site event at {event.point}")
        self.beachline.insert_arc(event.point, event.y)
        print("Beachline:", self.beachline)

    def handle_circle_event(self, event):
        print(f"Circle event at {event.point}")
        # Circle event logic will be added later

    def compute(self):
        self.process_events()
        # TODO: Clip edges to bounding box
        return self.edges

def fortune_voronoi(points):
    algo = FortuneVoronoi(points)
    return algo.compute()

if __name__ == "__main__":
    points = [(100, 400), (300, 300), (200, 100)]
    fortune_voronoi(points)
