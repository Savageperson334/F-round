# fading
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file book_chapters/noscale.py, line 734
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def fading(c: np.ndarray) -> float:
    """
    How many steps beyond the first a likeness takes to fall to 1/e of what it is
    at one step: read between the two distances it falls between, on a
    logarithmic scale. NaN if it never falls that far within MAX_R steps.
    """
    target = c[0] / np.e
    for r in range(1, len(c)):
        if c[r] <= target:
            if c[r] <= 0:
                return float(r - 1 + (c[r - 1] - target) / (c[r - 1] - c[r]))
            return float(r - 1 + np.log(c[r - 1] / target) / np.log(c[r - 1] / c[r]))
    return float("nan")
