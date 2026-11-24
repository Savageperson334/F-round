# human_bytesize
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/util.py, line 2464
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def human_bytesize(value):

    exts = 'Bytes kB MB GB TB PB EB ZB YB'.split()

    if value == 1:
        return '1 Byte'

    for i, ext in enumerate(exts):
        x = float(value) / 1000**i
        if round(x) < 10. and not value < 1000:
            return '%.1f %s' % (x, ext)
        if round(x) < 1000.:
            return '%.0f %s' % (x, ext)

    return '%i Bytes' % value
