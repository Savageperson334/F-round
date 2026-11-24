# fillup_zeros
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/io/ims.py, line 269
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def fillup_zeros(s, fmt):
    s = s.rstrip()
    if not s:
        return s

    if fmt == '%Y/%m/%d %H:%M:%S.3FRAC':
        return s + '0000/01/01 00:00:00.000'[len(s):]
    elif fmt == '%Y/%m/%d %H:%M:%S.2FRAC':
        return s + '0000/01/01 00:00:00.00'[len(s):]

    return s
