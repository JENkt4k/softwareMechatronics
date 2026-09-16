"""Bounded point-site Voronoi diagrams using Fortune's event sweep.

The sweep discovers neighboring sites via site/circle events. Each discovered
bisector is then clipped against the bounding box and nearest-site half-planes.
A linked beachline and explicit clipping favor clarity over asymptotic speed:
worst-case O(n**2) time, O(n) sweep storage. No third-party dependency is needed.

Coordinates use floating-point predicates, not exact arithmetic. Normalize first
to reduce scale/translation sensitivity; features below 1e-12 of the overall
coordinate span can be lost. Output contains internal cell boundaries only,
not the bounding-box perimeter. Duplicate sites are ignored.
"""

import heapq
import itertools
import math

from composites.geometry.beachline import BeachLine

_EPS = 1e-12


class Event:
    """A downward sweep event; site events precede circle events at equal y."""

    _ids = itertools.count()

    def __init__(self, y, point, site_event=True, arc=None, center=None):
        self.y = y
        self.point = point
        self.site_event = site_event
        self.arc = arc
        self.center = center
        self.valid = True
        self._order = next(self._ids)

    def __lt__(self, other):
        return (-self.y, not self.site_event, self.point[0], self._order) < (
            -other.y, not other.site_event, other.point[0], other._order
        )


def _point(value):
    try:
        x, y = value
        point = (float(x), float(y))
    except (TypeError, ValueError, OverflowError) as exc:
        raise ValueError("Each site must contain two finite coordinates") from exc
    if not all(math.isfinite(v) for v in point):
        raise ValueError("Each site must contain two finite coordinates")
    return point


class FortuneVoronoi:
    """Compute edges as [((x1, y1), (x2, y2)), ...] inside bbox.

    bbox is (xmin, ymin, xmax, ymax), with finite, strictly increasing bounds.
    Sites may lie outside it. Empty/single-site input returns no internal edges.
    compute() is repeatable. step() exposes valid events for demonstrations;
    its event and beachline coordinates are normalized, use to_world() to plot.
    vertices contains unique endpoints of the clipped output edges.
    """

    def __init__(self, points, bbox=(0, 0, 500, 500)):
        try:
            xmin, ymin, xmax, ymax = map(float, bbox)
        except (TypeError, ValueError, OverflowError) as exc:
            raise ValueError("bbox must contain four finite bounds") from exc
        if not all(math.isfinite(v) for v in (xmin, ymin, xmax, ymax)):
            raise ValueError("bbox must contain four finite bounds")
        if xmin >= xmax or ymin >= ymax:
            raise ValueError("bbox must have xmin < xmax and ymin < ymax")
        self.bbox = (xmin, ymin, xmax, ymax)
        self.points = sorted(set(_point(p) for p in points), key=lambda p: (-p[1], p[0]))
        xs = [xmin, xmax] + [p[0] for p in self.points]
        ys = [ymin, ymax] + [p[1] for p in self.points]
        self._origin = (min(xs) / 2 + max(xs) / 2, min(ys) / 2 + max(ys) / 2)
        self._scale = max(max(xs) - min(xs), max(ys) - min(ys))
        if not math.isfinite(self._scale):
            raise ValueError("Coordinate span is too large for floating-point arithmetic")
        self._sites = [self._normalize(p) for p in self.points]
        self._bbox = (*self._normalize((xmin, ymin)), *self._normalize((xmax, ymax)))
        self.events = [Event(p[1], p) for p in self._sites]
        heapq.heapify(self.events)
        self.beachline = BeachLine()
        self.edges = []
        self.vertices = []
        self.sweep_y = math.inf
        self._pairs = set()
        self._computed = False
        self.site_events = 0
        self.circle_events = 0

    def _normalize(self, p):
        return ((p[0] - self._origin[0]) / self._scale,
                (p[1] - self._origin[1]) / self._scale)

    def to_world(self, p):
        return (p[0] * self._scale + self._origin[0],
                p[1] * self._scale + self._origin[1])

    def _pair(self, a, b):
        if a != b:
            self._pairs.add(tuple(sorted((a, b))))

    @staticmethod
    def _invalidate(arc):
        if arc is not None and arc.circle_event is not None:
            arc.circle_event.valid = False
            arc.circle_event = None

    def _schedule(self, arc):
        self._invalidate(arc)
        if arc is None or arc.prev is None or arc.next is None:
            return
        a, b, c = arc.prev.site, arc.site, arc.next.site
        if a == c:
            return
        ax, ay = a[0] - b[0], a[1] - b[1]
        cx, cy = c[0] - b[0], c[1] - b[1]
        cross = ax * cy - ay * cx
        # Ordered arcs disappear only for clockwise site triples. Expressed
        # about the middle site, this is a positive determinant.
        if cross <= 0:
            return
        aa, cc = ax * ax + ay * ay, cx * cx + cy * cy
        ux = (aa * cy - cc * ay) / (2 * cross)
        uy = (ax * cc - cx * aa) / (2 * cross)
        center = (b[0] + ux, b[1] + uy)
        y = center[1] - math.hypot(ux, uy)
        if not math.isfinite(y) or not all(map(math.isfinite, center)):
            return
        if y > self.sweep_y + _EPS:
            return
        event = Event(min(y, self.sweep_y), (center[0], y), False, arc, center)
        arc.circle_event = event
        heapq.heappush(self.events, event)

    def handle_site_event(self, event):
        self.site_events += 1
        p = event.point
        if self.beachline.head is None:
            self.beachline.append(p)
            return
        # Initial horizontal sites have degenerate parabolas. Ordered events
        # append their arcs directly; splitting them would create phantom arcs.
        if p[1] == self._sites[0][1]:
            new = self.beachline.append(p)
            self._pair(new.prev.site, p)
            return
        arc = self.beachline.find_arc_above(p[0], self.sweep_y)
        self._invalidate(arc)
        self._pair(arc.site, p)
        left, middle, right = self.beachline.split(arc, p)
        # right replaces the previous neighbor of its successor.
        for changed in (left, right, right.next):
            self._schedule(changed)

    def handle_circle_event(self, event):
        arc = event.arc
        if not event.valid or arc is None or not arc.alive or arc.circle_event is not event:
            return
        self.circle_events += 1
        left, right = arc.prev, arc.next
        self._invalidate(arc)
        self._invalidate(left)
        self._invalidate(right)
        self._pair(left.site, right.site)
        self.beachline.remove(arc)
        self._schedule(left)
        self._schedule(right)

    def step(self):
        """Process one valid event, returning it, or None when finished."""
        while self.events:
            event = heapq.heappop(self.events)
            if not event.valid:
                continue
            self.sweep_y = event.y
            if event.site_event:
                self.handle_site_event(event)
            else:
                self.handle_circle_event(event)
            return event
        return None

    def process_events(self):
        while self.step() is not None:
            pass

    def _clip_bisector(self, p, q):
        """Intersect one bisector with box and all nearest-site half-planes."""
        mid = ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)
        dx, dy = q[0] - p[0], q[1] - p[1]
        length = math.hypot(dx, dy)
        direction = (-dy / length, dx / length)
        low, high = -math.inf, math.inf
        xmin, ymin, xmax, ymax = self._bbox
        constraints = [(1., 0., xmax - mid[0]), (-1., 0., mid[0] - xmin),
                       (0., 1., ymax - mid[1]), (0., -1., mid[1] - ymin)]
        for r in self._sites:
            if r == p or r == q:
                continue
            rx, ry = r[0] - p[0], r[1] - p[1]
            # |x-p|^2 <= |x-r|^2, centered at the bisector midpoint.
            bound = (rx * rx + ry * ry) / 2 - (mid[0] - p[0]) * rx - (mid[1] - p[1]) * ry
            constraints.append((rx, ry, bound))
        for nx, ny, bound in constraints:
            slope = nx * direction[0] + ny * direction[1]
            tolerance = _EPS * math.hypot(nx, ny)
            if abs(slope) <= tolerance:
                if bound < -tolerance:
                    return None
            elif slope > 0:
                high = min(high, bound / slope)
            else:
                low = max(low, bound / slope)
            if low > high:
                return None
        if high - low <= _EPS:
            return None  # point contacts are vertices, not edges
        ends = []
        for t in (low, high):
            x, y = mid[0] + t * direction[0], mid[1] + t * direction[1]
            ends.append((min(xmax, max(xmin, x)), min(ymax, max(ymin, y))))
        return tuple(sorted(ends))

    def compute(self):
        if self._computed:
            return list(self.edges)
        self.process_events()
        normalized_edges = []
        for pair in sorted(self._pairs):
            edge = self._clip_bisector(*pair)
            if edge is not None:
                normalized_edges.append(edge)
        # Merge numerically equivalent endpoints so cocircular sites share one
        # vertex. Neighboring grid buckets avoid rounding-boundary artifacts.
        buckets = {}

        def canonical(point):
            key = tuple(math.floor(v / _EPS) for v in point)
            for ix in range(key[0] - 1, key[0] + 2):
                for iy in range(key[1] - 1, key[1] + 2):
                    for known in buckets.get((ix, iy), ()):
                        if math.hypot(point[0] - known[0], point[1] - known[1]) <= _EPS:
                            return known
            buckets.setdefault(key, []).append(point)
            return point

        edges = set()
        for edge in normalized_edges:
            start, end = (canonical(p) for p in edge)
            if start != end:
                edges.add(tuple(sorted((self.to_world(start), self.to_world(end)))))
        self.edges = sorted(edges)
        self.vertices = sorted(set(p for edge in self.edges for p in edge))
        self._computed = True
        return list(self.edges)


def fortune_voronoi(points, bbox=(0, 0, 500, 500)):
    """Return bounded internal Voronoi edges for finite 2D point sites."""
    return FortuneVoronoi(points, bbox).compute()
