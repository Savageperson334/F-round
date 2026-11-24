# bounding_box_covering_points
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/dataset/gshhg.py, line 180
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def bounding_box_covering_points(points):
    lats = points[:, 0]
    lat_min, lat_max = num.min(lats), num.max(lats)

    lons = points[:, 1]
    lons = lons % 360.
    lon_min, lon_max = num.min(lons), num.max(lons)
    if lon_max - lon_min < 180.:
        return lon_min, lon_max, lat_min, lat_max

    lons = (lons - 180.) % 360. - 180.
    lon_min, lon_max = num.min(lons), num.max(lons)
    if lon_max - lon_min < 180.:
        return lon_min, lon_max, lat_min, lat_max

    return (-180., 180., lat_min, lat_max)
