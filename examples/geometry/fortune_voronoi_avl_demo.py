"""Animate the actual Fortune sweep (legacy filename retained for compatibility).

The implementation now uses a linked beachline. Frames include both site and
circle events; the last frame shows computed, clipped diagram edges.
"""

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

from composites.geometry.beachline import breakpoint
from composites.geometry.fortune_voronoi import FortuneVoronoi


def animate_beachline(points, bbox=(0, 0, 500, 500), show=True):
    algo = FortuneVoronoi(points, bbox)
    frames = []
    while True:
        event = algo.step()
        if event is None:
            break
        frames.append((event.y, event.site_event, [arc.site for arc in algo.beachline]))
    edges = algo.compute()
    fig, ax = plt.subplots()

    def update(index):
        ax.clear()
        ax.set_xlim(bbox[0], bbox[2])
        ax.set_ylim(bbox[1], bbox[3])
        ax.set_aspect("equal", adjustable="box")
        if algo.points:
            xs, ys = zip(*algo.points)
            ax.scatter(xs, ys, color="black", label="Sites")
        if index == len(frames):
            for start, end in edges:
                ax.plot([start[0], end[0]], [start[1], end[1]], "r-")
            ax.set_title("Completed bounded Voronoi diagram")
        else:
            level, is_site, sites = frames[index]
            # Just below the event, new parabolas are non-degenerate.
            directrix = level - 1e-8
            ax.axhline(algo.to_world((0, directrix))[1], color="blue", linestyle="--")
            for i, site in enumerate(sites):
                left = breakpoint(sites[i-1], site, directrix) if i else -float("inf")
                right = breakpoint(site, sites[i+1], directrix) if i+1 < len(sites) else float("inf")
                world_left = max(bbox[0], algo.to_world((left, 0))[0])
                world_right = min(bbox[2], algo.to_world((right, 0))[0])
                if world_left >= world_right:
                    continue
                # Evaluate in world units for display, with focus/directrix
                # differences computed in normalized coordinates for stability.
                xs = np.linspace(world_left, world_right, 150)
                normalized_x = np.array([algo._normalize((x, bbox[1]))[0] for x in xs])
                ys = ((normalized_x-site[0])**2 / (2*(site[1]-directrix))
                      + (site[1]+directrix)/2)
                world_y = [algo.to_world((0, y))[1] for y in ys]
                ax.plot(xs, world_y, "g-")
            ax.set_title("Fortune sweep: " + ("site event" if is_site else "circle event"))
        return ax.lines

    animation = FuncAnimation(fig, update, frames=len(frames)+1, interval=650,
                              repeat=False, blit=False)
    if show:
        plt.show()
    return fig, animation


# Existing users can keep the original entry point.
animate_avl_beachline = animate_beachline


if __name__ == "__main__":
    animate_beachline([(100, 400), (300, 300), (400, 200), (200, 100)])
