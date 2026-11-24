# dec
#
# Copied verbatim from https://github.com/isod89/clipper-fm1
#   file tools/gen_drumkits.py, line 38
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#   the same function also appears in: isod89/clipper-pro, jbschooley/Virtual-FM-1
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def dec(ms):                       # DECAY_K: 5 ms .. 4 s, index 0..127
    ms = max(5.0, min(4000.0, ms))
    return int(round(127 * math.log(ms / 5.0) / math.log(800)))
