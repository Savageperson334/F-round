# base36decode
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/util.py, line 2027
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def base36decode(number):
    '''
    Decode base36 endcoded positive integer.
    '''

    return int(number, 36)
