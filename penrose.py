import matplotlib as mpl
import itertools
from shapely.geometry import LineString, Polygon, MultiPoint, Point
from shapely import plotting
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

"""
Original coordinates (t, r, \theta, \varphi)

Converting this to a 1+1D picture using: u=t-r, v=t+r and compactifying it using u_tan = arctan(u) and v_tan = arctan(v)

Structure of Penrose
--------------------
* Gamma surface t-surface; r=0 (v-u=0)
* Null-infinity and timelike infinity
"""
# mpl.use("pgf")
custom_rcparams = {
    "figure.dpi": 200,
    "font.size": 6,
    "axes.labelsize": 6,
    "axes.labelweight": "bold",
    "axes.titlesize": 6,
    # Figure
    "figure.autolayout": True,
    "figure.titlesize": 7,
    # "figure.figsize": set_size(510.78302, fraction=0.5),
    "figure.figsize": (4.15, 4.15), #set_size(600, fraction=0.5),
    "savefig.format": "pdf",
    "lines.linewidth": 1,
    # Legend
    "legend.fontsize": 6,
    # "legend.frameon": False,
    # Ticks
    "xtick.labelsize": 6,
    "ytick.labelsize": 6,
    "xtick.minor.visible": True,
    "xtick.direction": "in",
    "ytick.direction": "in",
    "ytick.minor.visible": True,
    # Spines
    "axes.spines.left":   True,
    "axes.spines.bottom": True,
    "axes.spines.top":    True,
    "axes.spines.right":  True,
    # TeX
    "font.family": "serif",
    "text.usetex": True,
    # "pgf.texsystem": "lualatex",
    # "pgf.rcfonts": False,
    # "pgf.preamble": r"""
    #                 \usepackage{fontspec}
    #                 \usepackage[american]{babel}
    #                 \usepackage{amsmath}
    #                 \usepackage{mathtools}
    #                 \usepackage[per-mode=reciprocal]{siunitx}
    #                 \usepackage[
    #                     math-style=ISO,
    #                     bold-style=ISO,
    #                     nabla=upright,
    #                     partial=upright,
    #                     mathrm=sym,
    #                     ]{unicode-math}
    #                 """,
}

mpl.rcParams.update(custom_rcparams)
class Infty:
    def __init__(self, x, y, label):
        self.x = x
        self.y = y
        self.label = label
        pass
    
    @property
    def xy(self):
        return (self.x, self.y)
    
    def __repr__(self):
        return f"<{self.label}: {self.x, self.y}>"
    pass

def penrose_diamond(length=5):
    timelike_infties = (Infty(0, length, r"$i^+$"), Infty(0, -length, r"$i^-$"))
    spacelike_infties = (Infty(length, 0, r"$i^0$"), Infty(-length, 0, r"$i^0$"))

    diamond = Polygon([x.xy for pair in itertools.zip_longest(timelike_infties, spacelike_infties) for x in pair if x is not None])
    plotting.plot_polygon(diamond, add_points=False, edgecolor='black', facecolor='lightgray')
    plt.scatter(*timelike_infties[0].xy, facecolors='none', edgecolors='red', label='timelike infinity')
    plt.scatter(*timelike_infties[1].xy, facecolors='none', edgecolors='red', label='timelike infinity')
    plt.scatter(*spacelike_infties[0].xy, facecolors='none', edgecolors='blue', label='spacelike infinity')
    plt.scatter(*spacelike_infties[1].xy, facecolors='none', edgecolors='blue', label='spacelike infinity')

    
    plt.text(spacelike_infties[0].x + 0.05, spacelike_infties[0].y + 0.4, spacelike_infties[0].label, fontsize=12)
    plt.text(spacelike_infties[1].x - 0.4, spacelike_infties[1].y + 0.4, spacelike_infties[1].label, fontsize=12)
    plt.text(timelike_infties[0].x + 0.2, timelike_infties[0].y + 0.1, timelike_infties[0].label, fontsize=12)
    plt.text(timelike_infties[1].x + 0.2, timelike_infties[1].y - 0.4, timelike_infties[1].label, fontsize=12)

    plt.text((length/2 + 0.05), (length/2 + 0.05), r"$\mathcal{I}^+_R$", fontsize=12)
    plt.text(-(length/2 + 1), (length/2 + 0.05), r"$\mathcal{I}^+_L$", fontsize=12)
    plt.text((length/2 + 0.25), -(length/2 + 0.1), r"$\mathcal{I}^-_R$", fontsize=12)
    plt.text(-(length/2 + 1), -(length/2 + 0.1), r"$\mathcal{I}^-_L$", fontsize=12)
    # plt.text(timelike_infties[1].x + 0.2, timelike_infties[1].y - 0.4, timelike_infties[1].label, fontsize=12)

    """
    null_outgoing_1
    null_ingoing_1
    """
    null_hyps = [
        (LineString(([-length, -length], [length, length])), "u=0"),
        (LineString(([-length, length], [length, -length])), "v=0"),
    ]
    null, label = null_hyps[0]
    lineintersection = null.intersection(penrose)
    plt.plot(*lineintersection.xy, color="C12", label=label)
    midpoint = lineintersection.interpolate(0.25, normalized=True)
    # plt.text(midpoint.x, midpoint.y + 0.5, label, fontsize=10, ha='center', va='center', rotation=45)

    null, label = null_hyps[1]
    lineintersection = null.intersection(penrose)
    plt.plot(*lineintersection.xy, color="C13", label=label)
    midpoint = lineintersection.interpolate(0.25, normalized=True)
    # plt.text(midpoint.x, midpoint.y - 0.5, label, fontsize=10, ha='center', va='center', rotation=-45)
    return diamond

def penrose_triangle(length=5):
    timelike_infties = (Infty(0, length, r"$i^+$"), Infty(0, -length, r"$i^-$"))
    spacelike_infties = (Infty(length, 0, r"$i^0$"),)

    penrose = Polygon([x.xy for pair in itertools.zip_longest(timelike_infties, spacelike_infties) for x in pair if x is not None])
    plotting.plot_polygon(penrose, add_points=False, edgecolor='black', facecolor='lightgray')
    plt.scatter(*timelike_infties[0].xy, facecolors='none', edgecolors='red', label='timelike infinity')
    plt.scatter(*timelike_infties[1].xy, facecolors='none', edgecolors='red', label='timelike infinity')
    plt.scatter(*spacelike_infties[0].xy, facecolors='none', edgecolors='blue', label='spacelike infinity')

    
    plt.text(timelike_infties[0].x + 0.2, timelike_infties[0].y + 0.1, timelike_infties[0].label, fontsize=12)
    plt.text(timelike_infties[1].x + 0.2, timelike_infties[1].y - 0.4, timelike_infties[1].label, fontsize=12)
    plt.text(spacelike_infties[0].x + 0.05, spacelike_infties[0].y + 0.4, spacelike_infties[0].label, fontsize=12)

    plt.text((length/2 + 0.05), (length/2 + 0.05), r"$\mathcal{I}^+$", fontsize=12)
    plt.text((length/2 + 0.25), -(length/2 + 0.1), r"$\mathcal{I}^-$", fontsize=12)

    """
    null_outgoing_1
    null_ingoing_1
    """
    null_hyps = [
        (LineString(([0, 0], [length, length])), "u=0"),
        # LineString(([0, 0], [-length, length])),
        (LineString(([0, 0], [length, -length])), "v=0"),
        # LineString(([0, 0], [-length, -length]))
    ]
    null, label = null_hyps[0]
    lineintersection = null.intersection(penrose)
    plt.plot(*lineintersection.xy, color="C12", label=label)
    midpoint = lineintersection.interpolate(0.5, normalized=True)
    plt.text(midpoint.x, midpoint.y + 0.5, label, fontsize=10, ha='center', va='center', rotation=45)

    null, label = null_hyps[1]
    lineintersection = null.intersection(penrose)
    plt.plot(*lineintersection.xy, color="C13", label=label)
    midpoint = lineintersection.interpolate(0.5, normalized=True)
    plt.text(midpoint.x, midpoint.y - 0.5, label, fontsize=10, ha='center', va='center', rotation=-45)
    return penrose


def plot_hys(t, r, penrose):
    hypsurface = LineString([(x, y) for x, y in zip(t, r)])
    intersection = hypsurface.intersection(penrose)
    plt.plot(*intersection.xy)

length = 5
penrose = penrose_diamond()

r = np.linspace(-length, length, 100)
t = np.sqrt(r**2 + 1)
plot_hys(t, r, penrose)
plot_hys(-t, r, penrose)

plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.gca().set_aspect('equal')
plt.grid(False)
plt.show()
