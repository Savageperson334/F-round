# normalize_degrees
#
# Copied verbatim from https://github.com/franklinbaldo/digicomp
#   file vendor/moira/coordinates_reference.py, line 85
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def normalize_degrees(angle: float) -> float:
    """Reduce an angle to [0, 360)."""
    result = angle % 360.0
    # IEEE 754: a tiny negative value added to 360.0 may not underflow the
    # representable floor, leaving result == 360.0.  Clamp it back to 0.
    return 0.0 if result >= 360.0 else result
