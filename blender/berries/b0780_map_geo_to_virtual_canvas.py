# map_geo_to_virtual_canvas
#
# Copied verbatim from https://github.com/ZXCurban/NetOrbit
#   file src/netorbit/world_map.py, line 325
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

VIRTUAL_DOT_HEIGHT = 4

VIRTUAL_DOT_WIDTH = 2

WORLD_MAX_LAT = 90.0

WORLD_MAX_LON = 180.0

WORLD_MIN_LAT = -90.0

WORLD_MIN_LON = -180.0


def clamp(value: int, minimum: int, maximum: int) -> int:
    return max(minimum, min(maximum, value))


def map_geo_to_virtual_canvas(
    lat: float,
    lon: float,
    map_width: int,
    map_height: int,
) -> tuple[int, int]:
    """Map GPS coordinates to the Braille overlay's 2x4 virtual-dot grid."""
    virtual_width = max(1, map_width * VIRTUAL_DOT_WIDTH)
    virtual_height = max(1, map_height * VIRTUAL_DOT_HEIGHT)
    normalized_lon = ((lon - WORLD_MIN_LON) % 360.0) + WORLD_MIN_LON
    if normalized_lon == WORLD_MIN_LON and lon > 0:
        normalized_lon = WORLD_MAX_LON
    clamped_lat = max(WORLD_MIN_LAT, min(WORLD_MAX_LAT, lat))
    x = int((normalized_lon - WORLD_MIN_LON) / (WORLD_MAX_LON - WORLD_MIN_LON) * virtual_width)
    y = int((WORLD_MAX_LAT - clamped_lat) / (WORLD_MAX_LAT - WORLD_MIN_LAT) * virtual_height)
    return clamp(x, 0, virtual_width - 1), clamp(y, 0, virtual_height - 1)
