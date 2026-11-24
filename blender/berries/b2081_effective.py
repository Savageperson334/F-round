# effective
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file research/oee/checks/diversity.py, line 333
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def effective(counts: np.ndarray) -> float:
    p = counts / counts.sum()
    return float(1.0 / (p ** 2).sum())
