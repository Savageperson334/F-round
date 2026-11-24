# pairs_of
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file research/screen/measures.py, line 94
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def pairs_of(n: int, pairs) -> np.ndarray:
    """Links as pairs of places in the list of agents, each once, none from an agent to itself."""
    p = np.asarray(pairs, dtype=np.int64).reshape(-1, 2)
    p = p[(p[:, 0] != p[:, 1]) & (p >= 0).all(axis=1) & (p < n).all(axis=1)]
    return np.unique(np.sort(p, axis=1), axis=0)
