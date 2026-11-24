# deg_to_km_factors
#
# Copied verbatim from https://github.com/aaspip/pyekfmm
#   file pyekfmm/coordinates.py, line 4
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def deg_to_km_factors(lat_deg):
    """
    Return (km_per_deg_lat, km_per_deg_lon) at the given latitude (degrees).
    Uses mean Earth radius approximation.
    Accurate to ~0.1% for most latitudes.
    """
    # mean radius of Earth in km (WGS84 mean)
    R = 6371.0088  # km

    # 1 deg in radians
    deg_rad = math.pi / 180.0

    # km per degree latitude: arc length = R * dtheta
    km_per_deg_lat = R * deg_rad

    # km per degree longitude: depends on cosine(latitude)
    km_per_deg_lon = R * math.cos(math.radians(lat_deg)) * deg_rad

    return km_per_deg_lat, km_per_deg_lon
