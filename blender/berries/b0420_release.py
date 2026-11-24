# release
#
# Copied verbatim from https://github.com/KHAVld/ARTIHIVE
#   file tools/gen_dsp_tables.py, line 20
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math

FS = 44100


def release(lo, hi):
    return [max(1, round((1 - math.exp(-math.log(1000) / (lo * (hi / lo) ** (i / 127) * FS))) * (1 << 24)))
            for i in range(128)]
