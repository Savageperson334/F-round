# pulse
#
# Copied verbatim from https://github.com/isod89/clipper-fm1
#   file tools/gen_fmx.py, line 45
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#   the same function also appears in: isod89/clipper-pro
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math

N = 1024

TAU = 2 * math.pi


def additive(amps):
    v = [sum(a * math.sin(TAU * k * i / N + ph) for k, a, ph in amps) for i in range(N)]
    pk = max(abs(x) for x in v)
    return [int(round(32767 * x / pk)) for x in v]


def pulse(nh, w=0.25):
    return additive([(k, math.sin(math.pi * k * w) / k * (0.5 + 0.5 * math.cos(math.pi * k / (nh + 1))), -math.pi / 2)
                     for k in range(1, nh + 1)])
