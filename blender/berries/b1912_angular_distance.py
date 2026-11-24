# angular_distance
#
# Copied verbatim from https://github.com/franklinbaldo/digicomp
#   file vendor/moira/coordinates_reference.py, line 93
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def angular_distance(a: float, b: float) -> float:
    """Shortest unsigned arc between two longitudes (0–180°).

    Reduce the magnitude of the difference before folding at 180 degrees.
    A negative remainder would first add 360 and then subtract it again,
    introducing avoidable rounding at closed aspect-orb boundaries.
    """
    diff = abs(a - b) % 360.0
    return diff if diff <= 180.0 else 360.0 - diff
