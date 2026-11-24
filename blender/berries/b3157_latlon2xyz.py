# latlon2xyz
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/geometry.py, line 79
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num

d2r = num.pi/180.


def rtp2xyz(rtp):
    r = rtp[:, 0]
    theta = rtp[:, 1]
    phi = rtp[:, 2]
    vecs = num.empty(rtp.shape, dtype=num.float64)
    vecs[:, 0] = r*num.sin(theta)*num.cos(phi)
    vecs[:, 1] = r*num.sin(theta)*num.sin(phi)
    vecs[:, 2] = -r*num.cos(theta)
    return vecs


def latlon2xyz(latlon, radius=1.0):
    rtp = num.empty((latlon.shape[0], 3))
    rtp[:, 0] = radius
    rtp[:, 1] = (latlon[:, 0] + 90.) * d2r
    rtp[:, 2] = latlon[:, 1] * d2r
    return rtp2xyz(rtp)
