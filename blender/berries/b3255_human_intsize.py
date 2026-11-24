# human_intsize
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/util.py, line 2481
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def human_intsize(value):

    exts = 'x k M G T P E Z Y'.split()

    for i, ext in enumerate(exts):
        x = float(value) / 1000**i
        if round(x) < 10. and not value < 1000:
            return '%.1f%s' % (x, ' ' + ext if ext != 'x' else '')
        if round(x) < 1000.:
            return '%.0f%s' % (x, ' ' + ext if ext != 'x' else '')

    return '%i' % value
