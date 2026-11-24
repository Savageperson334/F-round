# spec_organ
#
# Copied verbatim from https://github.com/isod89/clipper-fm1
#   file tools/gen_vector.py, line 42
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#   the same function also appears in: isod89/clipper-pro
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def spec_organ(k):                                  # drawbars 16' 8' 4' 2 2/3' 2' (the fundamental here = 8')
    bars = {1: 1.0, 2: 0.8, 3: 0.55, 4: 0.5, 6: 0.3, 8: 0.25}
    return bars.get(k, 0.0), 0.0
