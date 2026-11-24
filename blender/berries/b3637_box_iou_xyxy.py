# box_iou_xyxy
#
# Copied verbatim from https://github.com/ssx12042/InsectsDetection
#   file utils/box_utils.py, line 22
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Moths insects and insect traps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def box_iou_xyxy(box1, box2):
    """
    计算两个矩形框的 IoU，矩形框的格式是 xyxy
    :param box1: 矩形框 1
    :param box2: 矩形框 2
    :return:
    """
    # tensor 转 ndarray
    # if type(box1) is paddle.Tensor:
    #     box1 = box1.numpy()
    # if type(box2) is paddle.Tensor:
    #     box2 = box2.numpy()

    # 获取 box1 左上角和右下角的坐标
    x1min, y1min, x1max, y1max = box1[0], box1[1], box1[2], box1[3]
    # 计算 box1 的面积
    s1 = (y1max - y1min + 1.) * (x1max - x1min + 1.)
    # 获取 box2 左上角和右下角的坐标
    x2min, y2min, x2max, y2max = box2[0], box2[1], box2[2], box2[3]
    # 计算 box2 的面积
    s2 = (y2max - y2min + 1.) * (x2max - x2min + 1.)

    # 计算相交矩形框的坐标
    xmin = np.maximum(x1min, x2min)
    ymin = np.maximum(y1min, y2min)
    xmax = np.minimum(x1max, x2max)
    ymax = np.minimum(y1max, y2max)
    # 计算相交矩形框的高度、宽度和面积
    inter_h = np.maximum(ymax - ymin + 1., 0.)
    inter_w = np.maximum(xmax - xmin + 1., 0.)
    intersection = inter_h * inter_w
    # 计算相并的面积
    union = s1 + s2 - intersection
    # 计算交并比
    iou = intersection / union
    return iou
