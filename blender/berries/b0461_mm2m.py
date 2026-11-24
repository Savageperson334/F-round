# mm2m
#
# Copied verbatim from https://github.com/MGross21/armctl
#   file armctl/utils/units.py, line 32
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Robots and tactile mechanisms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def mm2m(mm: float) -> float:
    """Convert millimeters to meters."""
    return mm * 1e-3
