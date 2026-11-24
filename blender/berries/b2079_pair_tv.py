# pair_tv
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file research/oee/checks/diversity.py, line 255
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def pair_tv(A: np.ndarray) -> float:
    """The mean total-variation distance between two different rows of A (shares over the same candidates)."""
    B = A.shape[0]
    if B < 2:
        return 0.0
    x = np.sort(A, axis=0)
    weights = (2 * np.arange(B) - B + 1)[:, None]
    return float(0.5 * (weights * x).sum() / (B * (B - 1) / 2))
