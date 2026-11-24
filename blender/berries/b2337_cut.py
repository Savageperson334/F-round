# cut
#
# Copied verbatim from https://github.com/isod89/clipper-fm1
#   file tools/gen_drumkits.py, line 43
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#   the same function also appears in: isod89/clipper-pro, jbschooley/Virtual-FM-1
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def cut(hz):                       # CUTOFF_HZ: 30 Hz .. 16 kHz
    hz = max(30.0, min(16000.0, hz))
    return int(round(127 * math.log(hz / 30.0) / math.log(16000 / 30)))
