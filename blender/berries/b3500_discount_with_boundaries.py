# discount_with_boundaries
#
# Copied verbatim from https://github.com/quantumiracle/Reinforcement_Learning_for_Traffic_Light_Control
#   file 6.ddpg_for_single/common/math_util.py, line 63
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Public transport and city motion
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def discount_with_boundaries(X, New, gamma):
    """
    X: 2d array of floats, time x features
    New: 2d array of bools, indicating when a new episode has started
    """
    Y = np.zeros_like(X)
    T = X.shape[0]
    Y[T-1] = X[T-1]
    for t in range(T-2, -1, -1):
        Y[t] = X[t] + gamma * Y[t+1] * (1 - New[t+1])
    return Y
