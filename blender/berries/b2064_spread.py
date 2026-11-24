# spread
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file research/atlas/profile.py, line 115
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def spread(values: np.ndarray) -> float:
    """The effective number of doubling classes the values fill: exp of the entropy of their shares."""
    v = np.asarray(values, dtype=float)
    v = v[v >= 1]
    if v.size == 0:
        return 0.0
    _, counts = np.unique(np.floor(np.log2(v)).astype(int), return_counts=True)
    p = counts / counts.sum()
    return float(np.exp(-(p * np.log(p)).sum()))
