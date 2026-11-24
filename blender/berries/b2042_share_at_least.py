# share_at_least
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file book_chapters/noscale.py, line 411
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def share_at_least(x: np.ndarray, grid: np.ndarray) -> np.ndarray:
    """For every value of the grid, the share of x at least that large."""
    s = np.sort(x)
    return 1.0 - np.searchsorted(s, grid, side="left") / len(s)
