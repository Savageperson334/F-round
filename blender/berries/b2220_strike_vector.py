# strike_vector
#
# Copied verbatim from https://github.com/hvasbath/beat
#   file beat/utility.py, line 921
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num

d2r = num.pi / 180.0


def strike_vector(strike, order="ENZ"):
    if order == "ENZ":
        return num.array([num.sin(strike * d2r), num.cos(strike * d2r), 0.0])
    elif order == "NEZ":
        return num.array([num.cos(strike * d2r), num.sin(strike * d2r), 0.0])
    else:
        raise Exception("Order %s not implemented!" % order)
