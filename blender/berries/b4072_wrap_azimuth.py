# wrap_azimuth
#
# Copied verbatim from https://github.com/ymatterlab/ycrystal
#   file src/ycrystal/core/lighting.py, line 221
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Molecular shapes and crystal lattices
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def wrap_azimuth(azimuth: float) -> float:
    """Wrap an angle in degrees to ``[-180, 180)``."""
    return float((azimuth + 180.0) % 360.0 - 180.0)
