# harmonic_mean
#
# Copied verbatim from https://github.com/pyrocko/qseek
#   file src/qseek/exporters/hypodd.py, line 1033
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def harmonic_mean(v0: float, gradient: float, z0: float, z1: float) -> float:
    """Harmonic mean of a linear velocity profile `v0 + gradient * z` from z0 to z1."""
    va, vb = v0 + gradient * z0, v0 + gradient * z1
    if math.isclose(va, vb):
        return (va + vb) / 2
    return (vb - va) / math.log(vb / va)
