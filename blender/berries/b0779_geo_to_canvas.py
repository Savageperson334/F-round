# geo_to_canvas
#
# Copied verbatim from https://github.com/ZXCurban/NetOrbit
#   file src/netorbit/world_map.py, line 314
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

WORLD_MAX_LAT = 90.0

WORLD_MAX_LON = 180.0

WORLD_MIN_LAT = -90.0

WORLD_MIN_LON = -180.0


def clamp(value: int, minimum: int, maximum: int) -> int:
    return max(minimum, min(maximum, value))


def geo_to_canvas(lat: float, lon: float, map_width: int, map_height: int) -> tuple[int, int]:
    """Map GPS coordinates to a terminal character grid using equirectangular projection."""
    normalized_lon = ((lon - WORLD_MIN_LON) % 360.0) + WORLD_MIN_LON
    if normalized_lon == WORLD_MIN_LON and lon > 0:
        normalized_lon = WORLD_MAX_LON
    clamped_lat = max(WORLD_MIN_LAT, min(WORLD_MAX_LAT, lat))
    x = int((normalized_lon - WORLD_MIN_LON) / (WORLD_MAX_LON - WORLD_MIN_LON) * map_width)
    y = int((WORLD_MAX_LAT - clamped_lat) / (WORLD_MAX_LAT - WORLD_MIN_LAT) * map_height)
    return clamp(x, 0, map_width - 1), clamp(y, 0, map_height - 1)
