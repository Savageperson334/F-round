# time2idx
#
# Copied verbatim from https://github.com/xumi1993/seispy
#   file seispy/hk.py, line 42
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def time2idx(times, ti0, dt):
    ti = ti0 + np.around(times / dt)
    return ti.reshape(ti.size).astype(int)
