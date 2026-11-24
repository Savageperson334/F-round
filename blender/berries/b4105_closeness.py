# closeness
#
# Copied verbatim from https://github.com/yukiyuqichen/His-Geo
#   notebook reproducible_code/code_for_table_1.ipynb (its code cells joined in order; line 22 of those)
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Historic cartography
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def closeness(x, n):
    if x <= n:
        return (np.cos(x*(np.pi/n))+1)/2
    else:
        return 0
