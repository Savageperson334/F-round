# ewrap
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/util.py, line 748
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def ewrap(lines, width=80, indent=''):
    lines = list(lines)
    if not lines:
        return ''
    fwidth = max(len(s) for s in lines)
    nx = max(1, (80-len(indent)) // (fwidth+1))
    i = 0
    rows = []
    while i < len(lines):
        rows.append(indent + ' '.join(x.ljust(fwidth) for x in lines[i:i+nx]))
        i += nx

    return '\n'.join(rows)
