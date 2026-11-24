# local_km_to_lonlat_equirectangular
#
# Copied verbatim from https://github.com/aaspip/pyekfmm
#   file pyekfmm/coordinates.py, line 59
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def local_km_to_lonlat_equirectangular(lon0, lat0, x, y):
    """
    Convert local Cartesian coordinates (km) back to geographic coordinates (lon, lat).
    lon0, lat0: reference point (degrees)
    x, y: local coordinates in km
    """

    R = 6371.0  # km

    # Convert reference lat0 to radians
    lat0_rad = np.deg2rad(lat0)

    # Compute latitude
    lat = lat0 + (y / R) * (180/np.pi)

    # Compute longitude
    lon = lon0 + (x / (R * np.cos(lat0_rad))) * (180/np.pi)

    return lon, lat
