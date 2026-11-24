# mw_theoretical_core_max
#
# Copied verbatim from https://github.com/mbeher2200/DarkHours
#   file darkhours/milky_way.py, line 135
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Light pollution and night maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

_GALACTIC_CORE_DEC = -29.0


def mw_theoretical_core_max(lat: float) -> float:
    """Theoretical maximum altitude the galactic core can reach from this latitude."""
    return max(0.0, 90.0 - abs(lat - _GALACTIC_CORE_DEC))
