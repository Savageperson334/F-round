# cbtick
#
# Copied verbatim from https://github.com/hvasbath/beat
#   file beat/plotting/common.py, line 54
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def cbtick(x):
    rx = num.floor(x * 1000.0) / 1000.0
    return [-rx, rx]
