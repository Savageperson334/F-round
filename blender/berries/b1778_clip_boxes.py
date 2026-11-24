# clip_boxes
#
# Copied verbatim from https://github.com/falcon-xu/character_recognition
#   file code/ctpn/src/text_connector/utils.py, line 7
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def threshold(coords, min_, max_):
    return np.maximum(np.minimum(coords, max_), min_)


def clip_boxes(boxes, im_shape):
    """
    Clip boxes to image boundaries.

    Args:
        boxes(numpy.array):bounding box.
        im_shape(numpy.array): image shape.

    Return:
        boxes(numpy.array):boundding box after clip.
    """
    boxes[:, 0::2] = threshold(boxes[:, 0::2], 0, im_shape[1] - 1)
    boxes[:, 1::2] = threshold(boxes[:, 1::2], 0, im_shape[0] - 1)
    return boxes
