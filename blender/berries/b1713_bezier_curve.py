# bezier_curve
#
# Copied verbatim from https://github.com/ericmjl/nxviz
#   file nxviz/backends/plotly_backend.py, line 61
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def bezier_curve(points: np.ndarray, n_points: int = 50) -> np.ndarray:
    """Evaluate a Bezier curve at n_points given control points.

    Supports quadratic (3 points) and cubic (4 points) Bezier curves.
    """
    n_control = len(points)
    t = np.linspace(0, 1, n_points)

    if n_control == 2:
        result = np.outer(1 - t, points[0]) + np.outer(t, points[1])
    elif n_control == 3:
        result = (
            np.outer((1 - t) ** 2, points[0])
            + np.outer(2 * (1 - t) * t, points[1])
            + np.outer(t**2, points[2])
        )
    elif n_control == 4:
        result = (
            np.outer((1 - t) ** 3, points[0])
            + np.outer(3 * (1 - t) ** 2 * t, points[1])
            + np.outer(3 * (1 - t) * t**2, points[2])
            + np.outer(t**3, points[3])
        )
    else:
        result = points

    return result
