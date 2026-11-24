# knob_quadrant
#
# Copied verbatim from https://github.com/genkigenki/Speak37
#   file tools/gen_aa_keycaps.py, line 97
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#   the same function also appears in: jbschooley/Virtual-FM-1, kpalaniuk/gnomad-firmware, oscillr/LRRY
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def knob_quadrant(r):
    """(coverage nibbles, angle bytes) of the top-right quadrant, row j = dy (0 nearest the centre)"""
    cov, ang = [], []
    r0 = r - 2.0
    for j in range(r):
        for i in range(r):
            n = 0
            for sy in range(4):
                for sx in range(4):
                    dx, dy = i + (sx + 0.5) / 4, j + (sy + 0.5) / 4
                    d = math.hypot(dx, dy)
                    n += r0 <= d <= r
            cov.append(min(15, int(round(n * 15 / 16))))
            a = math.atan2(i + 0.5, j + 0.5)          # from 12 o'clock, clockwise: dx over dy (up)
            ang.append(min(255, int(a / (math.pi / 2) * 256)))
    return cov, ang
