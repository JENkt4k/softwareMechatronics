# fortune_voronoi_avl_demo.py
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from composites.geometry.fortune_voronoi import FortuneVoronoi


def parabola_points(site, y_sweep, x_range):
    """
    Compute parabola points for a site (focus) and sweep line y_sweep.
    Formula: y = ( (x - x0)^2 + y0^2 - y_sweep^2 ) / (2 * (y0 - y_sweep))
    """
    x0, y0 = site
    if y_sweep == y0:  # Degenerate case
        return None, None
    x = np.linspace(x_range[0], x_range[1], 200)
    y = ((x - x0)**2 + y0**2 - y_sweep**2) / (2 * (y0 - y_sweep))
    return x, y

def animate_avl_beachline(points, bbox=(0, 0, 500, 500)):
    algo = FortuneVoronoi(points, bbox=bbox)
    events = algo.events[:]

    fig, ax = plt.subplots()
    ax.set_xlim(bbox[0], bbox[2])
    ax.set_ylim(bbox[1], bbox[3])
    ax.set_title("AVL-Based Fortune Algorithm (Beach Line as Parabolas)")

    xs, ys = zip(*points)
    ax.scatter(xs, ys, color="red", s=50, label="Sites")

    sweep_line = ax.axhline(bbox[3], color="blue", linestyle="--", label="Sweep Line")
    parabola_lines = []
    ax.legend()

    def init():
        sweep_line.set_ydata([bbox[3], bbox[3]])
        for line in parabola_lines:
            line.remove()
        parabola_lines.clear()
        return [sweep_line]

    def update(frame):
        if frame < len(events):
            event = events[frame]
            y_sweep = event.y
            sweep_line.set_ydata([y_sweep, y_sweep])

            if event.site_event:
                algo.handle_site_event(event)

            # Clear old parabolas
            for line in parabola_lines:
                line.remove()
            parabola_lines.clear()

            # Draw parabolas for current arcs
            sites = [arc_node.site for arc_node in algo.beachline.tree.inorder_values()]
            for site in sites:
                x, y = parabola_points(site, y_sweep, (bbox[0], bbox[2]))
                if x is not None:
                    line, = ax.plot(x, y, 'g-', linewidth=1)
                    parabola_lines.append(line)

        return [sweep_line] + parabola_lines

    ani = animation.FuncAnimation(
        fig, update, frames=len(events),
        init_func=init, blit=False, repeat=False, interval=1000
    )

    plt.show()

if __name__ == "__main__":
    points = [(100, 400), (300, 300), (400, 200), (200, 100)]
    animate_avl_beachline(points)
