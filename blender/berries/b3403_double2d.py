# double2d
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/plot/gmtpy.py, line 1640
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def double2d(f):
    f2 = num.empty((f.shape[0]*2-1, f.shape[1]*2-1))
    f2[:, :] = num.nan
    f2[::2, ::2] = f
    f2[1::2, ::2] = (f[:-1, :] + f[1:, :])/2.
    f2[::2, 1::2] = (f[:, :-1] + f[:, 1:])/2.
    f2[1::2, 1::2] = (f[:-1, :-1] + f[1:, :-1] + f[:-1, 1:] + f[1:, 1:])/4.
    diag = f2[1::2, 1::2]
    diagA = (f[:-1, :-1] + f[1:, 1:]) / 2.
    diagB = (f[1:, :-1] + f[:-1, 1:]) / 2.
    f2[1::2, 1::2] = num.where(num.isnan(diag), diagA, diag)
    f2[1::2, 1::2] = num.where(num.isnan(diag), diagB, diag)
    return f2
