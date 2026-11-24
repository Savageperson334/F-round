# t_pulse_frame
#
# Copied verbatim from https://github.com/isod89/clipper-fm1
#   file tools/gen_wavetables.py, line 87
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#   the same function also appears in: isod89/clipper-pro
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math

NH = 128

TWO_PI = 2 * math.pi


def t_pulse_frame(w):
    return [(2 / (math.pi * h) * math.sin(TWO_PI * h * w), 2 / (math.pi * h) * (1 - math.cos(TWO_PI * h * w)))
            for h in range(1, NH + 1)]
