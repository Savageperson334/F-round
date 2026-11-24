# sshift
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/gf/seismosizer.py, line 796
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math
import numpy as num


def sshift(times, amplitudes, tshift, deltat):

    t0 = math.floor(tshift / deltat) * deltat
    t1 = math.ceil(tshift / deltat) * deltat
    if t0 == t1:
        return times, amplitudes

    amplitudes2 = num.zeros(amplitudes.size + 1, dtype=float)

    amplitudes2[:-1] += (t1 - tshift) / deltat * amplitudes
    amplitudes2[1:] += (tshift - t0) / deltat * amplitudes

    times2 = num.arange(times.size + 1, dtype=float) * \
        deltat + times[0] + t0

    return times2, amplitudes2
