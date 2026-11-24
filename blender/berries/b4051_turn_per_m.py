# turn_per_m
#
# Copied verbatim from https://github.com/ygd551/terra-incognita
#   file tools/tracking_report.py, line 23
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


def turn_per_m(P):
    """Mean |heading change| per metre on a 0.5 m resampling [deg/m] (0 for short pieces)."""
    v = np.diff(resample(P)[:, :2], axis=0)
    v = v[np.linalg.norm(v, axis=1) > 1e-3]
    if len(v) < 2:
        return 0.0
    return np.abs(np.degrees(np.diff(np.unwrap(np.arctan2(v[:, 1], v[:, 0]))))).sum() / (0.5 * len(v))
