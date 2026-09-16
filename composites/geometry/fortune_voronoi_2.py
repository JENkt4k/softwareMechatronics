"""Compatibility imports for the experimental Fortune sketch.

Use composites.geometry.fortune_voronoi for the canonical implementation.
"""

from .fortune_voronoi import Event, FortuneVoronoi, fortune_voronoi

__all__ = ["Event", "FortuneVoronoi", "fortune_voronoi"]
