# jround
#
# Copied verbatim from https://github.com/jbschooley/Virtual-FM-1
#   file engines/choralroot/upstream/tools/gen_layout.py, line 80
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def jround(x):
    """Math.round"""
    return math.floor(x + 0.5)
