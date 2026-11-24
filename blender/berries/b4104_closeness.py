# closeness
#
# Copied verbatim from https://github.com/yukiyuqichen/His-Geo
#   notebook reproducible_code/code_for_figure_6.ipynb (its code cells joined in order; line 7 of those)
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Historic cartography
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def closeness(x, n):
    """
    Calculate the closeness of the extracted result to the benchmark result
    :param x (km): geodesic distance between the extracted point and the benchmark point
    :param n (km): baseline distance (max geodesic distance inside the most accurate level polygon of the benchmark data)
    """
    if x <= n:
        return (np.cos(x*(np.pi/n))+1)/2
    else:
        return 0
