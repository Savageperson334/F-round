# upcoming_vectors
#
# Copied verbatim from https://github.com/donjpierce/traffic
#   file models.py, line 174
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Public transport and city motion
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math
import numpy as np


def upcoming_vectors(view):
    """
    determines the vectors between the nodes in a view

    :param     view:     tuple:  tuple (x,y) of lists representing n upcoming noce positions
    :return vectors:      list:  list of (n-1) vectors pointing between the nodes along the path of travel
    """
    vectors = []
    for i in range(len(view)):
        if i < len(view) - 1:
            vectors.append(np.array([
                view[i + 1][0] - view[i][0], view[i + 1][1] - view[i][1]]
            ) / math.sqrt(np.dot(view[i], view[i + 1])))
    return np.array(vectors)
