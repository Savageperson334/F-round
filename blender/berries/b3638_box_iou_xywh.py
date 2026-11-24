# box_iou_xywh
#
# Copied verbatim from https://github.com/ssx12042/InsectsDetection
#   file utils/box_utils.py, line 60
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Moths insects and insect traps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def box_iou_xywh(box1, box2):
    """
    计算两个矩形框的 IoU，矩形框的格式是 xywh
    :param box1: 矩形框 1
    :param box2: 矩形框 2
    :return:
    """
    x1min, y1min = box1[0] - box1[2] / 2., box1[1] - box1[3] / 2.
    x1max, y1max = box1[0] + box1[2] / 2., box1[1] + box1[3] / 2.
    s1 = box1[2] * box1[3]

    x2min, y2min = box2[0] - box2[2] / 2., box2[1] - box2[3] / 2.
    x2max, y2max = box2[0] + box2[2] / 2., box2[1] + box2[3] / 2.
    s2 = box2[2] * box2[3]

    xmin = np.maximum(x1min, x2min)
    ymin = np.maximum(y1min, y2min)
    xmax = np.minimum(x1max, x2max)
    ymax = np.minimum(y1max, y2max)
    inter_h = np.maximum(ymax - ymin, 0.)
    inter_w = np.maximum(xmax - xmin, 0.)
    intersection = inter_h * inter_w

    union = s1 + s2 - intersection
    iou = intersection / union
    return iou
