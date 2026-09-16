# Fortune sweep implementation

The public function `fortune_voronoi(points, bbox)` returns finite internal Voronoi edges as pairs of endpoint tuples. The class also exposes stepping and clipped endpoints for demonstrations. The core is standard-library Python.

## Event sweep

1. Normalize coordinates using the span and center of sites plus the bounding box. Deduplicate identical sites and order initial events by descending y, ascending x.
2. Maintain a doubly linked sequence of parabolic arcs. Locate a new site's arc by evaluating parabola intersections at the directrix, then split it into old/new/old arcs. Equal-height initial sites append directly.
3. For consecutive triples with the disappearing orientation, compute their circumcircle. Enqueue its bottommost point as a circle event. Adjacency changes invalidate obsolete events.
4. Remove a disappearing arc at a valid circle event and record the newly adjacent site pair. Reschedule the affected neighbors. Site events take precedence at an equal sweep height; queue sequence numbers resolve remaining ties deterministically.
5. Clip each discovered neighboring-site bisector to the bounding box and the half-planes in which its sites are nearest. This produces finite segments for bounded edges, unbounded rays, and full bisectors alike. Discard empty intervals and zero-length contacts. Merge numerically equivalent endpoints.

Clipping to all nearest-site half-planes avoids extrapolating uncertain ray directions at the end of the sweep. It is part of this implementation's quadratic cost. The algorithm does not substitute raster sampling or enumerate all site pairs in normal operation.

The event model follows the standard presentation in [Giri Narasimhan's computational geometry lecture notes](https://users.cs.fiu.edu/~giri/teach/UoM/7713/f98/voronoi.html). This implementation was written for this repository; no external implementation is vendored.

## Complexity and precision

Linked arc lookup is O(n); each of O(n) candidate bisectors is clipped against O(n) constraints. Total worst-case time is O(n^2), with O(n) auxiliary storage including the event queue, beachline, candidate neighbors, and output. A balanced search tree and direct ray/segment completion would be needed for the classic O(n log n) bound.

This is floating-point geometry, not exact-predicate geometry. Normalization improves translation/scale behavior, but extremely small features relative to the overall span (around 1e-12) can collapse. Exact duplicate input sites are removed. Horizontal, vertical, collinear, cocircular, exterior, and tied-height inputs are covered by tests. Nonfinite coordinates, invalid boxes, and overflowing coordinate spans are rejected.

Box boundary segments are not added as cell perimeter edges. An internal bisector coinciding with a box side can be returned; isolated corner contacts are discarded. `vertices` means unique endpoints of returned edges, including intersections with the box.

## Verification

The unit suite compares complete diagrams against an independent polygon-cell clipping oracle across analytic examples, random continuous inputs, and integer grids. It also checks equidistance/nearest-site invariants, clipping, event progression, repeatability, permutation invariance, and translation/scale transformations. The reference oracle does not call implementation geometry helpers. Optional SciPy comparisons can independently check the sweep's discovered neighboring sites.

Run all tests with `python -m unittest discover -s tests -v`. Plotting and SciPy remain optional extras, not runtime dependencies of the algorithm.
