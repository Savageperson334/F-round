# downsample_plan
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/gui/snuffler/snufflings/spectrogram.py, line 42
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def downsample_plan(n, n_max):
    n_mean = (n-1) // n_max + 1
    n_new = n // n_mean
    return n_new, n_mean
