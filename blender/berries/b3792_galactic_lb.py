# galactic_lb
#
# Copied verbatim from https://github.com/tjyank/orrery-tui
#   file orrery/stellar/coords.py, line 42
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math

Vec3 = tuple[float, float, float]


def galactic_lb(v: Vec3) -> tuple[float, float]:
    """Galactic longitude and latitude, in degrees, of a galactic Cartesian vector."""
    r = math.sqrt(v[0] ** 2 + v[1] ** 2 + v[2] ** 2)
    if r < 1e-12:
        return 0.0, 0.0
    return math.degrees(math.atan2(v[1], v[0])) % 360.0, math.degrees(math.asin(max(-1.0, min(1.0, v[2] / r))))
