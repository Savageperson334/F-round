# aslist
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/response.py, line 303
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def aslist(x):
    if x is None:
        return []

    try:
        return list(x)
    except TypeError:
        return [x]
