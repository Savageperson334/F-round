# desat
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/gui/snuffler/snufflings/spectrogram.py, line 16
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def desat(c, a):
    cmean = (c[0] + c[1] + c[2]) / 3.
    return tuple(cc*a + cmean*(1.0-a) for cc in c)
