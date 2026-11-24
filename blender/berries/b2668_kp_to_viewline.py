# kp_to_viewline
#
# Copied verbatim from https://github.com/mbeher2200/DarkHours
#   file darkhours/aurora.py, line 163
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Light pollution and night maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

VIEWLINE_DEG_PER_KP  = 2.05

VIEWLINE_KP0_MAGLAT  = 66.5


def kp_to_viewline(kp: float) -> float:
    """Geomagnetic latitude of the equatorward edge of overhead aurora."""
    return VIEWLINE_KP0_MAGLAT - VIEWLINE_DEG_PER_KP * kp
