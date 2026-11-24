# format_luminosity
#
# Copied verbatim from https://github.com/tjyank/orrery-tui
#   file orrery/stellar/app.py, line 48
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def format_luminosity(lum: float) -> str:
    """Visual luminosity in Suns, readable at both ends of the range."""
    if lum < 0.01:
        return f"1/{1 / lum:,.0f} of the Sun"
    if abs(lum - 1) < 0.005:
        return "1 Sun"
    return f"{lum:.3g} Suns"
