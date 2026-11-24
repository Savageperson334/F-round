# cluster
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file research/oee/checks/diversity.py, line 303
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def cluster(dist: np.ndarray, floor: float) -> np.ndarray:
    """
    Average-linkage grouping, merged while the closest two groups are no further
    apart than the noise floor: a kind is brains no more different from one
    another than a brain is from itself.
    """
    n = dist.shape[0]
    label = np.arange(n)
    groups = {i: [i] for i in range(n)}
    d = dist.copy().astype(float)
    np.fill_diagonal(d, np.inf)
    alive = np.ones(n, dtype=bool)
    while alive.sum() > 1:
        sub = np.where(alive[:, None] & alive[None, :], d, np.inf)
        i, j = np.unravel_index(np.argmin(sub), sub.shape)
        if sub[i, j] > floor:
            break
        ni, nj = len(groups[i]), len(groups[j])
        d[i, :] = (d[i, :] * ni + d[j, :] * nj) / (ni + nj)
        d[:, i] = d[i, :]
        d[i, i] = np.inf
        alive[j] = False
        d[j, :] = np.inf
        d[:, j] = np.inf
        groups[i] += groups.pop(j)
    for g, members in enumerate(groups.values()):
        label[members] = g
    return label
