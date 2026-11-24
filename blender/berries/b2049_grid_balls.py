# grid_balls
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file book_chapters/scaledims.py, line 255
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math
import numpy as np


def grid_balls(dim: int, radius: int) -> np.ndarray:
    """The points of an endless grid within r steps of one, r = 0 … radius: Σₖ 2ᵏ·C(dim, k)·C(r, k)."""
    return np.array([sum(2 ** k * math.comb(dim, k) * math.comb(r, k) for k in range(dim + 1))
                     for r in range(radius + 1)], float)
