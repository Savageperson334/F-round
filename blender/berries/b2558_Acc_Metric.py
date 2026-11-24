# Acc_Metric
#
# Copied verbatim from https://github.com/liaochengcsu/BCE-Net
#   file utils/seg_metric.py, line 60
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Historic cartography
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def Acc_Metric(Mask,GT):
    GT_pos_sum = np.sum(GT == 1)
    Mask_pos_sum = np.sum(Mask == 1)
    True_pos_sum = np.sum((GT == 1) * (Mask == 1))
    Precision = float(True_pos_sum) / (Mask_pos_sum + 1e-6)
    Recall = float(True_pos_sum) / (GT_pos_sum + 1e-6)
    IoU = float(True_pos_sum) / (GT_pos_sum + Mask_pos_sum - True_pos_sum + 1e-6)
    # IoU = Precision * Recall / (Precision + Recall - Precision * Recall + 1e-6)
    if GT_pos_sum==0 and Mask_pos_sum==0:
        IoU =1
    F1_score = 2 * Precision * Recall / (Precision + Recall + 1e-6)
    # return Recall,Precision,F1_score,IoU
    return F1_score
