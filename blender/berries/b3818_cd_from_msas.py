# cd_from_msas
#
# Copied verbatim from https://github.com/topherchris420/nocturne
#   file vdl7/skyglow.py, line 65
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Light pollution and night maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def cd_from_msas(m: float) -> float:
    """Luminance (cd/m^2) of a sky of m mag/arcsec^2 (V band)."""
    return 10.8e4 * 10 ** (-0.4 * m)
