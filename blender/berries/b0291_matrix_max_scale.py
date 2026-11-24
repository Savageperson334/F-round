# matrix_max_scale
#
# Copied verbatim from https://github.com/Hansolox80/a1-mini-pen-plotter
#   file app/core/svg_parser.py, line 194
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Plotters & drawing machines
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math
import numpy as np


def matrix_max_scale(matrix: np.ndarray) -> float:
    """Computes the maximum singular value (linear scale factor) of the 2x2 upper-left submatrix."""
    sub = matrix[:2, :2]
    try:
        s = np.linalg.svd(sub, compute_uv=False)
        val = float(np.max(s))
        if not math.isfinite(val):
            return 1.0
        return max(1e-6, min(val, 1e6))
    except Exception:
        return 1.0
