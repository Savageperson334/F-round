# find_index
#
# Copied verbatim from https://github.com/MartinThoma/hwrt
#   file hwrt/partitions.py, line 90
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def find_index(segmentation, stroke_id):
    """
    >>> find_index([[0, 1, 2], [3, 4], [5, 6, 7]], 0)
    0
    >>> find_index([[0, 1, 2], [3, 4], [5, 6, 7]], 1)
    0
    >>> find_index([[0, 1, 2], [3, 4], [5, 6, 7]], 5)
    2
    >>> find_index([[0, 1, 2], [3, 4], [5, 6, 7]], 6)
    2
    """
    for i, symbol in enumerate(segmentation):
        for sid in symbol:
            if sid == stroke_id:
                return i
    return -1
