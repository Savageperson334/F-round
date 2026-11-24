# nice_seconds_floor
#
# Copied verbatim from https://github.com/hvasbath/beat
#   file beat/apps/beatdown.py, line 58
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#   the same function also appears in: pyrocko/pyrocko
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def nice_seconds_floor(s):
    nice = [
        1.0,
        10.0,
        60.0,
        600.0,
        3600.0,
        3.0 * 3600.0,
        12 * 3600.0,
        24 * 3600.0,
        48 * 3600.0,
    ]
    p = s
    for x in nice:
        if s < x:
            return p

        p = x

    return s
