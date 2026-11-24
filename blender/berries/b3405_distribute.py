# distribute
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/plot/gmtpy.py, line 2059
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def distribute(sizes, grows, space):
    sizes = list(sizes)
    gsum = sum(grows)
    if gsum > 0.0:
        for i in range(len(sizes)):
            sizes[i] += space*grows[i]/gsum
    return sizes
