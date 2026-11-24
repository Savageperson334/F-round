# sky_lux
#
# Copied verbatim from https://github.com/topherchris420/nocturne
#   file vdl7/bench.py, line 20
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Light pollution and night maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def sky_lux(elev_deg: float) -> float:
    """Horizontal illuminance from solar elevation, rough but monotonic."""
    if elev_deg > 0:
        return 100.0 + 100_000.0 * math.sin(math.radians(elev_deg))
    if elev_deg > -6:
        return 100.0 * 10 ** (elev_deg / 2.0)        # civil twilight, 100 -> 0.1 lx
    return 0.05
