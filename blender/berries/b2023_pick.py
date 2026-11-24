# pick
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file explain_minimal.py, line 114
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def pick(scores: np.ndarray) -> int:
    """Which of several — the best one."""
    return int(np.argmax(scores))
