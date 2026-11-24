# nmi
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file research/atlas/flowpersist.py, line 94
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def nmi(a: np.ndarray, b: np.ndarray) -> float:
    """Normalised mutual information of two labellings of the same agents: 2 I / (H_a + H_b)."""
    n = len(a)
    if n == 0:
        return float("nan")
    _, ia = np.unique(a, return_inverse=True)
    _, ib = np.unique(b, return_inverse=True)
    joint = np.unique(ia.astype(np.int64) * (ib.max() + 1) + ib, return_counts=True)[1] / n
    pa = np.bincount(ia) / n
    pb = np.bincount(ib) / n
    h = lambda p: float(-(p[p > 0] * np.log(p[p > 0])).sum())
    ha, hb, hab = h(pa), h(pb), h(joint)
    return 2.0 * (ha + hb - hab) / (ha + hb) if ha + hb > 0 else 1.0
