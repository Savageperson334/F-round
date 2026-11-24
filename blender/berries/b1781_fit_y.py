# fit_y
#
# Copied verbatim from https://github.com/falcon-xu/character_recognition
#   file code/ctpn/src/text_connector/utils.py, line 56
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def fit_y(X, Y, x1, x2):
    if np.sum(X == X[0]) == len(X):
        return Y[0], Y[0]
    p = np.poly1d(np.polyfit(X, Y, 1))
    return p(x1), p(x2)
