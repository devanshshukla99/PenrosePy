import matplotlib as mpl
import itertools
from shapely.geometry import LineString, Polygon, MultiPoint, Point
from shapely import plotting
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from penrose.mpl_config import custom_rcparams
from dataclasses import dataclass

"""
Original coordinates (t, r, \theta, \varphi)

Converting this to a 1+1D picture using: u=t-r, v=t+r and compactifying it using u_tan = arctan(u) and v_tan = arctan(v)

Structure of Penrose
--------------------
* Gamma surface t-surface; r=0 (v-u=0)
* Null-infinity and timelike infinity
"""

mpl.rcParams.update(custom_rcparams)


@dataclass
class Infty:
    x: float
    y: float
    label: str

    @property
    def xy(self):
        return (self.x, self.y)

    def __repr__(self):
        return f"<{self.label}: {self.x, self.y}>"

    pass


class PenrosePy:
    def __init__(self, length: int, plot_text: bool = True, draw_null: bool = False):
        self.length = length
        self._plot_text = plot_text
        self._draw_null = draw_null
        pass

    def penrose_diamond(self):
        timelike_infties = (Infty(0, self.length, r"$i^+$"), Infty(0, -self.length, r"$i^-$"))
        spacelike_infties = (Infty(self.length, 0, r"$i^0$"), Infty(-self.length, 0, r"$i^0$"))

        self.structure = Polygon(
            [
                x.xy
                for pair in itertools.zip_longest(timelike_infties, spacelike_infties)
                for x in pair
                if x is not None
            ]
        )
        plotting.plot_polygon(self.structure, add_points=False, edgecolor="black", facecolor="lightgray")
        plt.scatter(*timelike_infties[0].xy, facecolors="none", edgecolors="red", label="timelike infinity")
        plt.scatter(*timelike_infties[1].xy, facecolors="none", edgecolors="red", label="timelike infinity")
        plt.scatter(
            *spacelike_infties[0].xy, facecolors="none", edgecolors="blue", label="spacelike infinity"
        )
        plt.scatter(
            *spacelike_infties[1].xy, facecolors="none", edgecolors="blue", label="spacelike infinity"
        )

        if self.plot_text:
            plt.text(
                spacelike_infties[0].x + 0.05,
                spacelike_infties[0].y + 0.4,
                spacelike_infties[0].label,
                fontsize=12,
            )
            plt.text(
                spacelike_infties[1].x - 0.4,
                spacelike_infties[1].y + 0.4,
                spacelike_infties[1].label,
                fontsize=12,
            )
            plt.text(
                timelike_infties[0].x + 0.2,
                timelike_infties[0].y + 0.1,
                timelike_infties[0].label,
                fontsize=12,
            )
            plt.text(
                timelike_infties[1].x + 0.2,
                timelike_infties[1].y - 0.4,
                timelike_infties[1].label,
                fontsize=12,
            )

            plt.text((self.length / 2 + 0.05), (self.length / 2 + 0.05), r"$\mathcal{I}^+_R$", fontsize=12)
            plt.text(-(self.length / 2 + 1), (self.length / 2 + 0.05), r"$\mathcal{I}^+_L$", fontsize=12)
            plt.text((self.length / 2 + 0.25), -(self.length / 2 + 0.1), r"$\mathcal{I}^-_R$", fontsize=12)
            plt.text(-(self.length / 2 + 1), -(self.length / 2 + 0.1), r"$\mathcal{I}^-_L$", fontsize=12)
            # plt.text(timelike_infties[1].x + 0.2, timelike_infties[1].y - 0.4, timelike_infties[1].label, fontsize=12)

        # Null hypersurfaces
        null_hyps = [
            (LineString(([-self.length, -self.length], [self.length, self.length])), "u=0"),  # null outgoing
            (LineString(([-self.length, self.length], [self.length, -self.length])), "v=0"),  # null ingoing
        ]
        null, label = null_hyps[0]
        lineintersection = null.intersection(self.structure)
        plt.plot(*lineintersection.xy, color="C12", label=label)
        midpoint = lineintersection.interpolate(0.25, normalized=True)
        # plt.text(midpoint.x, midpoint.y + 0.5, label, fontsize=10, ha='center', va='center', rotation=45)

        null, label = null_hyps[1]
        lineintersection = null.intersection(self.structure)
        plt.plot(*lineintersection.xy, color="C13", label=label)
        midpoint = lineintersection.interpolate(0.25, normalized=True)
        # plt.text(midpoint.x, midpoint.y - 0.5, label, fontsize=10, ha='center', va='center', rotation=-45)
        return

    def penrose_triangle(self):
        r_surface = LineString(([0, 0], [self.length, 0]))
        gamma_surface = LineString(([0, 0], [0, self.length]))

        timelike_infties = (Infty(0, self.length, r"$i^+$"), Infty(0, -self.length, r"$i^-$"))
        spacelike_infties = (Infty(self.length, 0, r"$i^0$"),)

        self.structure = Polygon(
            [
                x.xy
                for pair in itertools.zip_longest(timelike_infties, spacelike_infties)
                for x in pair
                if x is not None
            ]
        )
        plotting.plot_polygon(self.structure, add_points=False, edgecolor="black", facecolor="lightgray")
        plt.scatter(*timelike_infties[0].xy, facecolors="none", edgecolors="red", label="timelike infinity")
        plt.scatter(*timelike_infties[1].xy, facecolors="none", edgecolors="red", label="timelike infinity")
        plt.scatter(
            *spacelike_infties[0].xy, facecolors="none", edgecolors="blue", label="spacelike infinity"
        )

        if self._plot_text:
            plt.text(
                timelike_infties[0].x + 0.15 * self.length / 4,
                timelike_infties[0].y + 0.1 * self.length / 4,
                timelike_infties[0].label,
                fontsize=12,
            )
            plt.text(
                timelike_infties[1].x + 0.15 * self.length / 4,
                timelike_infties[1].y - 0.35 * self.length / 4,
                timelike_infties[1].label,
                fontsize=12,
            )
            plt.text(
                spacelike_infties[0].x - 0.1 * self.length / 4,
                spacelike_infties[0].y + 0.4 * self.length / 4,
                spacelike_infties[0].label,
                fontsize=12,
            )

            plt.text(
                (self.length / 2 + 0.05 * self.length / 2),
                (self.length / 2 + 0.05 * self.length / 2),
                r"$\mathcal{I}^+$",
                fontsize=12,
            )
            plt.text(
                (self.length / 2 + 0.25 * self.length / 2),
                -(self.length / 2 + 0.1 * self.length / 2),
                r"$\mathcal{I}^-$",
                fontsize=12,
            )

        # Null hypersurfaces
        if self._draw_null:
            null_hyps = [
                (LineString(([0, 0], [self.length, self.length])), "u=0"),  # null outgoing
                (LineString(([0, 0], [self.length, -self.length])), "v=0"),  # null ingoing
            ]
            null, label = null_hyps[0]
            lineintersection = null.intersection(self.structure)
            plt.plot(*lineintersection.xy, color=(0.477504, 0.821444, 0.318195, 1.0), label=label)
            midpoint = lineintersection.interpolate(0.5, normalized=True)
            if self.plot_text:
                plt.text(
                    midpoint.x, midpoint.y + 0.25, label, fontsize=10, ha="center", va="center", rotation=45
                )

            null, label = null_hyps[1]
            lineintersection = null.intersection(self.structure)
            plt.plot(*lineintersection.xy, color=(0.282623, 0.140926, 0.457517, 1.0), label=label)
            midpoint = lineintersection.interpolate(0.5, normalized=True)
            if self.plot_text:
                plt.text(
                    midpoint.x, midpoint.y - 0.25, label, fontsize=10, ha="center", va="center", rotation=-45
                )

        # Dashed-r-surface
        plt.plot(*r_surface.xy, "--", color="black")
        return

    def _plot_hypersurface(self, r, t, *args, **kwargs):
        hypsurface = LineString([(x, y) for x, y in zip(r, t)])
        intersection = hypsurface.intersection(self.structure)
        plt.plot(*intersection.xy, *args, **kwargs)

    def plot_hypersurface(self, r, t, *args, **kwargs):
        u_tilde = np.arctan(t - r)  # *self.length
        v_tilde = np.arctan(t + r)  # *self.length

        theta = np.radians(45)  # Convert angle to radians
        rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

        rotated_v_tilde, rotated_u_tilde = np.dot(rotation_matrix, np.array([v_tilde, u_tilde]))
        hypsurface = LineString([(x, y) for x, y in zip(rotated_v_tilde, rotated_u_tilde)])
        intersection = hypsurface.intersection(self.structure)
        if intersection.geom_type != "LineString":
            raise UserWarning("Intersection is not a point, be ware")
        plt.plot(*intersection.xy, *args, **kwargs)

    def show(self, *args, **kwargs):
        plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
        plt.gca().set_aspect("equal")
        plt.grid(False)
        plt.show(*args, **kwargs)

    pass
