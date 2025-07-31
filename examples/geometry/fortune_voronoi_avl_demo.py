import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from composites.geometry.fortune_voronoi import FortuneVoronoi

def parabola_points(site, y_sweep, x_range):
    """
    Compute parabola points for a site (focus) and sweep line y_sweep.
    Formula:
        y = ((x - x0)^2 + y0^2 - y_sweep^2) / (2 * (y0 - y_sweep))
    """
    x0, y0 = site
    if y_sweep == y0:
        return None, None
    x = np.linspace(x_range[0], x_range[1], 300)
    y = ((x - x0)**2 + y0**2 - y_sweep**2) / (2 * (y0 - y_sweep))
    return x, y

def vertical_bisector(p1, p2, bbox):
    """
    Calculate vertical bisector (perpendicular to line connecting p1 and p2).
    Returns x, y for a line segment clipped to bbox.
    """
    x1, y1 = p1
    x2, y2 = p2
    mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
    dx, dy = x2 - x1, y2 - y1

    if dx == 0:  # vertical line, bisector is horizontal
        x_vals = np.linspace(bbox[0], bbox[2], 50)
        y_vals = np.full_like(x_vals, mid_y)
    elif dy == 0:  # horizontal line, bisector is vertical
        y_vals = np.linspace(bbox[1], bbox[3], 50)
        x_vals = np.full_like(y_vals, mid_x)
    else:
        slope = -dx / dy
        y_vals = np.linspace(bbox[1], bbox[3], 50)
        x_vals = mid_x + (y_vals - mid_y) * slope
    return x_vals, y_vals

def animate_avl_beachline(points, bbox=(0, 0, 500, 500)):
    algo = FortuneVoronoi(points, bbox=bbox)
    events = algo.events[:]

    fig, ax = plt.subplots()
    ax.set_xlim(bbox[0], bbox[2])
    ax.set_ylim(bbox[1], bbox[3])
    ax.set_title("AVL-Based Fortune Algorithm (Parabolas & Bisectors)")

    xs, ys = zip(*points)
    ax.scatter(xs, ys, color="red", s=50, label="Sites")

    sweep_line = ax.axhline(bbox[3], color="blue", linestyle="--", label="Sweep Line")
    parabola_lines = []
    bisector_lines = []
    ax.legend()

    def init():
        sweep_line.set_ydata([bbox[3], bbox[3]])
        for line in parabola_lines + bisector_lines:
            line.remove()
        parabola_lines.clear()
        bisector_lines.clear()
        return [sweep_line]

    def update(frame):
        if frame < len(events):
            event = events[frame]
            y_sweep = event.y
            sweep_line.set_ydata([y_sweep, y_sweep])

            if event.site_event:
                algo.handle_site_event(event)

            # Remove old lines
            for line in parabola_lines + bisector_lines:
                line.remove()
            parabola_lines.clear()
            bisector_lines.clear()

            # Draw parabolas for current arcs
            sites = [arc_node.site for arc_node in algo.beachline.tree.inorder_values()]
            for site in sites:
                x, y = parabola_points(site, y_sweep, (bbox[0], bbox[2]))
                if x is not None:
                    line, = ax.plot(x, y, 'g-', linewidth=1)
                    parabola_lines.append(line)

            # Draw bisectors between adjacent sites
            for i in range(len(sites) - 1):
                x_bis, y_bis = vertical_bisector(sites[i], sites[i + 1], bbox)
                line, = ax.plot(x_bis, y_bis, 'm--', linewidth=1)
                bisector_lines.append(line)

        return [sweep_line] + parabola_lines + bisector_lines

    ani = animation.FuncAnimation(
        fig, update, frames=len(events),
        init_func=init, blit=False, repeat=False, interval=1000
    )

    plt.show()

if __name__ == "__main__":
    points = [(100, 400), (300, 300), (400, 200), (200, 100)]
    animate_avl_beachline(points)
