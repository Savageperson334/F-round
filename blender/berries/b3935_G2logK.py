# G2logK
#
# Copied verbatim from https://github.com/worm-portal/pychnosz
#   file pychnosz/models/hkf_helpers.py, line 85
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Metrology, microscopes and geology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def G2logK(G, Tc):
    # Gas constant R is in cal/mol K
    return G / (-math.log(10) * 1.9872 * (273.15+Tc))
