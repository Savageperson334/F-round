# gcd
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/util.py, line 1233
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def gcd(a, b, epsilon=1e-7):
    '''
    Greatest common divisor.
    '''

    while b > epsilon*a:
        a, b = b, a % b

    return a
