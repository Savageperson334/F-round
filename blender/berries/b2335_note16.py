# note16
#
# Copied verbatim from https://github.com/isod89/clipper-fm1
#   file tools/gen_drumkits.py, line 28
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#   the same function also appears in: isod89/clipper-pro, jbschooley/Virtual-FM-1
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def note16(hz):                    # MIDI note and 1/16 semitones
    n = 69 + 12 * math.log2(hz / 440.0)
    n16 = max(0, min(127 * 16 + 15, int(round(n * 16))))
    return n16 >> 4, n16 & 15
