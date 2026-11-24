# xyz_to_latlon
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/orthodrome.py, line 1412
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num
import math

d2r = math.pi/180.

r2d = 1./d2r


def xyz_to_latlon(xyz):
    if xyz.ndim == 1:
        return xyz_to_latlon(xyz[num.newaxis, :])[0]

    latlons = num.zeros((xyz.shape[0], 2))
    latlons[:, 0] = num.arctan2(
        xyz[:, 2], num.sqrt(xyz[:, 0]**2 + xyz[:, 1]**2)) * r2d
    latlons[:, 1] = num.arctan2(
        xyz[:, 1], xyz[:, 0]) * r2d
    return latlons
