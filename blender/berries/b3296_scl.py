# scl
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/fomosto/qseis.py, line 73
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def scl(cs):
    if not cs:
        return '\n#'

    return '\n'+' '.join('(%e,%e)' % (c.real, c.imag) for c in cs)
