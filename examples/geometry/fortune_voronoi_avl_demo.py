# fortune_voronoi_avl_demo.py
"""
Visualization of the sweep line and AVL-based beach line for Fortune's Algorithm.
This version animates:
- Site points.
- Sweep line descending.
- Beach line arcs as vertical markers (simplified placeholder).
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from composites.geometry.fortune_voronoi import FortuneVoronoi

def animate_avl_beachline(points, bbox=(0, 0, 500, 500)):
    algo = FortuneVoronoi(points, bbox=bbox)
    events = algo.events[:]  # Copy initial events for visualization

    fig, ax = plt.subplots()
    ax.set_xlim(bbox[0], bbox[2])
    ax.set_ylim(bbox[1], bbox[3])
    ax.set_title("AVL-Based Fortune Algorithm (Sweep Line)")

    # Scatter plot of site points
    xs, ys = zip(*points)
    ax.scatter(xs, ys, color="red", s=50, label="Sites")

    sweep_line = ax.axhline(bbox[3], color="blue", linestyle="--", label="Sweep Line")
    beach_markers, = ax.plot([], [], 'go', label="Beach Arcs")

    ax.legend()

    def init():
      sweep_line.set_ydata([bbox[3], bbox[3]])
      beach_markers.set_data([], [])
      return sweep_line, beach_markers

    def update(frame):
      if frame < len(events):
          event = events[frame]
          sweep_line.set_ydata([event.y, event.y])  # Fixed sweep line update

          if event.site_event:
              algo.handle_site_event(event)

          # Beachline nodes are keys (x positions)
          nodes_x = list(algo.beachline.tree.inorder())
          nodes_y = [event.y] * len(nodes_x)
          beach_markers.set_data(nodes_x, nodes_y)

      return sweep_line, beach_markers


    ani = animation.FuncAnimation(fig, update, frames=len(events),
                                  init_func=init, blit=True, repeat=False, interval=1000)

    plt.show()

if __name__ == "__main__":
    points = [(100, 400), (300, 300), (200, 100), (400, 200)]
    animate_avl_beachline(points)
