# clo_factor
#
# Copied verbatim from https://github.com/topherchris420/nocturne
#   file vdl7/profiles.py, line 153
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Light pollution and night maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def clo_factor(burn_hours: float, new: float = 0.86, end_of_life_h: float = 100_000.0) -> float:
    """Constant light output: drive rises from 0.86 when new to 1.00 at
    100,000 h so delivered lumens stay flat as the LEDs depreciate."""
    f = max(0.0, min(1.0, burn_hours / end_of_life_h))
    return new + (1.0 - new) * f
