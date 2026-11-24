# cardinal
#
# Copied verbatim from https://github.com/mbeher2200/DarkHours
#   file darkhours/format_ctx.py, line 115
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Light pollution and night maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def cardinal(az_deg: float) -> str:
    """Convert an azimuth in degrees to an 8-point cardinal direction string."""
    dirs = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    return dirs[round(az_deg / 45) % 8]
