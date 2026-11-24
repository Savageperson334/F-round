# equatorial_xyz
#
# Copied verbatim from https://github.com/tjyank/orrery-tui
#   file orrery/stellar/coords.py, line 33
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math

Vec3 = tuple[float, float, float]


def equatorial_xyz(ra_deg: float, dec_deg: float, dist: float) -> Vec3:
    ra, dec = math.radians(ra_deg), math.radians(dec_deg)
    return (dist * math.cos(dec) * math.cos(ra), dist * math.cos(dec) * math.sin(ra), dist * math.sin(dec))
