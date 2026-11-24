# latlon_to_xyz
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/orthodrome.py, line 1399
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num
import math

d2r = math.pi/180.


def latlon_to_xyz(latlons):
    if latlons.ndim == 1:
        return latlon_to_xyz(latlons[num.newaxis, :])[0]

    points = num.zeros((latlons.shape[0], 3))
    lats = latlons[:, 0]
    lons = latlons[:, 1]
    points[:, 0] = num.cos(lats*d2r) * num.cos(lons*d2r)
    points[:, 1] = num.cos(lats*d2r) * num.sin(lons*d2r)
    points[:, 2] = num.sin(lats*d2r)
    return points
