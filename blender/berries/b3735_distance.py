# distance
#
# Copied verbatim from https://github.com/tferr/hIPNAT
#   file src/main/resources/scripts/Analyze/Skeleton/Classify_Particles_Using_Skeleton.py, line 85
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Microscopy & small worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def distance(x1, y1, x2, y2):
    """ Calculates the distance between 2D points """
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
