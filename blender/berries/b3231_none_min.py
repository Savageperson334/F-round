# none_min
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/trace.py, line 3403
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def none_min(li):
    if None in li:
        return None
    else:
        return min(x for x in li if x is not None)
