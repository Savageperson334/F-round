# spread
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file book_chapters/noscale.py, line 328
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def spread(x: np.ndarray) -> float:
    """How widely values vary, relative to their middle: (90th − 10th percentile) ÷ median."""
    q10, q50, q90 = np.quantile(x, [0.1, 0.5, 0.9])
    return float((q90 - q10) / q50) if q50 > 0 else float("nan")
