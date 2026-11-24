# resample
#
# Copied verbatim from https://github.com/ygd551/terra-incognita
#   file tools/tracking_report.py, line 14
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Cave surveys and subterranean maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def resample(P, step=0.5):
    P = np.asarray(P, float)
    s = np.r_[0, np.cumsum(np.linalg.norm(np.diff(P, axis=0), axis=1))]
    if s[-1] < step:
        return P[[0, -1]]
    q = np.arange(0, s[-1], step)
    return np.c_[[np.interp(q, s, P[:, k]) for k in range(P.shape[1])]].T
