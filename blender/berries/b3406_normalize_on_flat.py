# normalize_on_flat
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/plot/response.py, line 49
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def normalize_on_flat(f, tf, factor=10000.):
    df = num.diff(num.log(f))
    tap = 1.0 / (1.0 + factor * (num.diff(num.log(num.abs(tf)))/df)**2)
    return tf / (num.sum(num.abs(tf[1:]) * tap) / num.sum(tap))
