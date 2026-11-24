# locut_k
#
# Copied verbatim from https://github.com/oscillr/LRRY
#   file lrry/tools/gen_tables.py, line 28
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math

FS = 44100


def locut_k(f):
    if f <= 0:
        return 0
    c = math.cos(2 * math.pi * f / FS)
    a = (-c + math.sqrt(c * c + 3 - 4 * c)) / (3 - 4 * c)      # |H|^2 = 1/2:  (3 - 4c) a^2 + 2 c a - 1 = 0
    return int(round(32768 * (1 - a)))
