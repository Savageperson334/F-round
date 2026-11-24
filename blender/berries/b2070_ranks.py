# ranks
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file research/atlas/wolfram.py, line 370
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def ranks(a: np.ndarray) -> np.ndarray:
    """Ranks from 1, ties given their average rank."""
    a = np.asarray(a, float)
    r = np.empty(len(a))
    r[np.argsort(a, kind="mergesort")] = np.arange(1, len(a) + 1)
    _, inv, counts = np.unique(a, return_inverse=True, return_counts=True)
    return np.bincount(inv, weights=r)[inv] / counts[inv]
