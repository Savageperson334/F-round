# array_min2d
#
# Copied verbatim from https://github.com/quantumiracle/Reinforcement_Learning_for_Traffic_Light_Control
#   file 6.ddpg_for_single/ddpg/memory.py, line 35
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Public transport and city motion
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def array_min2d(x):
    x = np.array(x)
    if x.ndim >= 2:
        return x
    return x.reshape(-1, 1)
