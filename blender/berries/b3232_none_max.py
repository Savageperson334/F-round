# none_max
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/trace.py, line 3410
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def none_max(li):
    if None in li:
        return None
    else:
        return max(x for x in li if x is not None)
