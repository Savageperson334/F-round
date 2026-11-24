# haversine
#
# Copied verbatim from https://github.com/paudetseis/RfPy
#   file rfpy/ccp.py, line 1069
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def haversine(lat, lon, xs_lat, xs_lon):  # great-circle distance (kilometres)

    earth_radius = 6371.  # kilometres

    lat = np.radians(lat)
    lon = np.radians(lon)
    xs_lat = np.radians(xs_lat)
    xs_lon = np.radians(xs_lon)
    dlat = lat - xs_lat
    dlon = lon - xs_lon
    a = ((np.sin(dlat/2.))**2.) + \
        (np.cos(xs_lat)*np.cos(lat)*((np.sin(dlon/2.))**2.))
    distance = np.abs(2.*earth_radius*np.arcsin(np.sqrt(a)), dtype=float)

    return np.abs(distance)
