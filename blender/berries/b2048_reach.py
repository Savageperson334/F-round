# reach
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file book_chapters/scale.py, line 230
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def reach(row: np.ndarray) -> float:
    """The first distance at which two agents are no more often of one family than any two."""
    below = np.flatnonzero(row <= 1)
    return float(below[0] + 1) if below.size else float("nan")
