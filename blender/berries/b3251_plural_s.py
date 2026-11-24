# plural_s
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/util.py, line 1783
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def plural_s(n):
    if not isinstance(n, int):
        n = len(n)

    return 's' if n != 1 else ''
