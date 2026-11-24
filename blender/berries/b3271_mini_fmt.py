# mini_fmt
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/apps/cake.py, line 503
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def mini_fmt(v, d=5, try_fmts='fe'):
    for fmt in try_fmts:
        for i in range(d, -1, -1):
            s = ('%%%i.%i%s' % (d, i, fmt)) % v
            if len(s) <= d and (v == 0.0 or float(s) != 0.0):
                return s

    return s
