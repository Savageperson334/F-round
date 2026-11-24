# check_floor
#
# Copied verbatim from https://github.com/topherchris420/nocturne
#   file vdl7/schedule.py, line 46
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Light pollution and night maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def check_floor(unsensed_floor: float) -> float:
    """The unsensed floor is a share of full output: finite, 0-100 %."""
    if not (isinstance(unsensed_floor, (int, float)) and math.isfinite(unsensed_floor)
            and 0.0 <= unsensed_floor <= 100.0):
        raise ValueError(f"unsensed floor {unsensed_floor!r} must be a percentage from 0 to 100")
    return float(unsensed_floor)
