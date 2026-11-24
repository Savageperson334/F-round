# compute_sd_step
#
# Copied verbatim from https://github.com/kaist-ami/Paint-it
#   file paint_it.py, line 119
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Textures and materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def compute_sd_step(min, max, iter_frac):
    step = (max - (max - min) * math.sqrt(iter_frac))
    return step
