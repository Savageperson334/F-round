# fixdoublefloat
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/io/sac.py, line 26
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def fixdoublefloat(x):
    f = 10**math.floor(math.log10(x)) / 1000000.
    return round(x/f)*f
