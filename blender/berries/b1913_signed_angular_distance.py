# signed_angular_distance
#
# Copied verbatim from https://github.com/franklinbaldo/digicomp
#   file vendor/moira/coordinates_reference.py, line 104
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def signed_angular_distance(from_deg: float, to_deg: float) -> float:
    """Signed difference to_deg − from_deg in (−180, +180]."""
    diff = (to_deg - from_deg) % 360.0
    if diff > 180.0:
        diff -= 360.0
    return diff
