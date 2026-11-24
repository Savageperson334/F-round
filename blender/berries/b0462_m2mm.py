# m2mm
#
# Copied verbatim from https://github.com/MGross21/armctl
#   file armctl/utils/units.py, line 37
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Robots and tactile mechanisms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def m2mm(meters: float) -> float:
    """Convert meters to millimeters."""
    return meters * 1e3
