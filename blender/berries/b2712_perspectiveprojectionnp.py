# perspectiveprojectionnp
#
# Copied verbatim from https://github.com/meng-yijie1996/LBM-Ferrofluid
#   file renderutils/dibr/utils/perspective.py, line 72
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Ferrofluids and magnetic materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def perspectiveprojectionnp(fovy, ratio=1.0, near=0.01, far=10.0):

    tanfov = np.tan(fovy / 2.0)
    # top = near * tanfov
    # right = ratio * top
    # mtx = [near / right, 0, 0, 0, \
    #          0, near / top, 0, 0, \
    #          0, 0, -(far+near)/(far-near), -2*far*near/(far-near), \
    #          0, 0, -1, 0]
    mtx = [
        [1.0 / (ratio * tanfov), 0, 0, 0],
        [0, 1.0 / tanfov, 0, 0],
        [0, 0, -(far + near) / (far - near), -2 * far * near / (far - near)],
        [0, 0, -1.0, 0],
    ]
    # return np.array(mtx, dtype=np.float32)
    return np.array([[1.0 / (ratio * tanfov)], [1.0 / tanfov], [-1]], dtype=np.float32)
