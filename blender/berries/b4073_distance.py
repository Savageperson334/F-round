# distance
#
# Copied verbatim from https://github.com/ymatterlab/ycrystal
#   file src/ycrystal/core/measure.py, line 91
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Molecular shapes and crystal lattices
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def distance(a: np.ndarray, b: np.ndarray) -> float:
    """Return the distance between two points (same unit as the input, here Å)."""
    return float(np.linalg.norm(np.asarray(b, dtype=float) - np.asarray(a, dtype=float)))
