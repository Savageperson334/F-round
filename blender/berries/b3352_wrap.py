# wrap
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/io/stationxml.py, line 218
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def wrap(s, width=80, indent=4):
    words = s.split()
    lines = []
    t = []
    n = 0
    for w in words:
        if n + len(w) >= width:
            lines.append(' '.join(t))
            n = indent
            t = [' '*(indent-1)]

        t.append(w)
        n += len(w) + 1

    lines.append(' '.join(t))
    return '\n'.join(lines)
