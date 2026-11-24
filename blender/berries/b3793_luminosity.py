# luminosity
#
# Copied verbatim from https://github.com/tjyank/orrery-tui
#   file orrery/stellar/coords.py, line 62
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

SUN_ABS_MAG = 4.83


def luminosity(abs_mag: float) -> float:
    """Visual luminosity in Suns."""
    return 10 ** ((SUN_ABS_MAG - abs_mag) / 2.5)
