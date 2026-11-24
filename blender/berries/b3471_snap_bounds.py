# snap_bounds
#
# Copied verbatim from https://github.com/pyrocko/qseek
#   file src/qseek/tracers/fast_marching_3d/velocity_models.py, line 88
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def snap_bounds(
    bounds: tuple[float, float], grid_spacing: float, outward: bool
) -> tuple[float, float]:
    """Snap the end of bounds to a whole number of grid cells from the start.

    Args:
        bounds (tuple[float, float]): Start and end in [m].
        grid_spacing (float): Grid spacing in [m].
        outward (bool): Extend the bounds to cover them, else shrink them to stay
            inside.

    Returns:
        tuple[float, float]: The snapped bounds.
    """
    n_cells = (bounds[1] - bounds[0]) / grid_spacing
    n_cells = np.ceil(n_cells - 1e-6) if outward else np.floor(n_cells + 1e-6)
    return float(bounds[0]), float(bounds[0] + n_cells * grid_spacing)
