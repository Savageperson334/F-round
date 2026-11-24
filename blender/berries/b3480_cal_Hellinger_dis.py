# cal_Hellinger_dis
#
# Copied verbatim from https://github.com/qiaoguanren/TrafficGamer
#   notebook vis_argoverse2.ipynb (its code cells joined in order; line 132 of those)
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Public transport and city motion
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def cal_Hellinger_dis(P, Q):
    """
    Calculate the Hellinger distance for two distribution
    """
    # Convert into probability first
    P = P/np.sum(P)
    Q = Q/np.sum(Q)

    H_dist = (1 / np.sqrt(2)) * np.linalg.norm(np.abs(np.sqrt(P) - np.sqrt(Q)))
    return H_dist
