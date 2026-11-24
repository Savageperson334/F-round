# str_gain
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/response.py, line 162
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def str_gain(gain):
    if gain == 1.0:
        return 'one'
    elif isinstance(gain, complex):
        return 'gain{%s}' % repr(gain)
    else:
        return 'gain{%g}' % gain
