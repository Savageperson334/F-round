# inormalize
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/gui/sparrow/elements/table.py, line 22
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def inormalize(x, imin, imax, discrete=True):
    if x.size == 0:
        return num.full(x.shape, imin, dtype=int)

    xmin = num.nanmin(x)
    xmax = num.nanmax(x)
    if xmin == xmax:
        xmin -= 0.5
        xmax += 0.5

    rmin = imin - 0.5
    rmax = imax + 0.5

    if discrete:
        return num.clip(
            num.round(
                rmin + (x - xmin) * (
                    (rmax-rmin) / (xmax - xmin))).astype(num.int64),
            imin, imax)
    else:
        return num.clip(
            rmin + (x - xmin) * ((rmax-rmin) / (xmax - xmin)),
            imin, imax)
