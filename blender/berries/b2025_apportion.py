# apportion
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file explain_minimal.py, line 126
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def apportion(scores: np.ndarray, total: int) -> np.ndarray:
    """
    Split a whole number of tokens by score, losing none.

    Largest remainder: floor everything, then hand the leftovers to whoever was
    cut hardest. Tokens are conserved, so they cannot be rounded away.
    """
    scores = np.maximum(0.0, scores)                 # a negative score is no score
    if scores.sum() <= 0:
        scores = np.ones(len(scores))                 # no preference: an even split
    exact = scores / scores.sum() * total
    whole = np.floor(exact).astype(int)
    for i in np.argsort(-(exact - whole))[:total - int(whole.sum())]:
        whole[i] += 1
    return whole
