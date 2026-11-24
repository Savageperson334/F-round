# safe_float
#
# Copied verbatim from https://github.com/FilipDominec/nihilnovi
#   file robust_csv_parser.py, line 53
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def safe_float(string):
    try:                    return float(string)
    except:                 return np.nan
