# mix
#
# Copied verbatim from https://github.com/FartyPants/fm1-nachtfahrt
#   file tools/film_title.py, line 27
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def mix(a, b, t16):
    t = min(max(t16, 0.0), 16.0) / 16.0
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))
