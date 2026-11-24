# rank
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file gol_atlas.py, line 532
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def rank(v: np.ndarray) -> np.ndarray:
    """Ranks from 0, ties sharing the mean of the ranks they span."""
    _, inv, counts = np.unique(v, return_inverse=True, return_counts=True)
    stop = np.cumsum(counts)
    return ((stop - counts + stop - 1) / 2.0)[inv]
