# time_fmt_drumline
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/gui/drum/view.py, line 210
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def time_fmt_drumline(t):
    ti = int(t)
    if ti % 60 == 0:
        fmt = '%H:%M'
    else:
        fmt = '%H:%M:%S'

    if ti % (3600*24) == 0:
        fmt = fmt + ' %Y-%m-%d'

    return fmt
