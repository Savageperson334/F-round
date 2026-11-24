# haversine_km
#
# Copied verbatim from https://github.com/strangeloopcanon/paleontology_analytics
#   file thesis/_lib/__init__.py, line 124
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Fossil measurements and paleontology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def haversine_km(lat1: float, lng1: float, lat2: float, lng2: float) -> float:
    """Great-circle distance in km between two points (WGS-84 mean radius)."""
    r = 6371.0088
    lat1, lng1, lat2, lng2 = (
        math.radians(v) for v in (lat1, lng1, lat2, lng2)
    )
    dlat = lat2 - lat1
    dlng = lng2 - lng1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlng / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))
