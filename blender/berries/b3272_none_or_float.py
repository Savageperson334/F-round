# none_or_float
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/apps/colosseo.py, line 85
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def none_or_float(x):
    if x == 'none':
        return None
    else:
        return float(x)
