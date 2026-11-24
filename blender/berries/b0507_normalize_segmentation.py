# normalize_segmentation
#
# Copied verbatim from https://github.com/MartinThoma/hwrt
#   file hwrt/partitions.py, line 158
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def normalize_segmentation(segmentation):
    for i in range(len(segmentation)):
        segmentation[i] = sorted(segmentation[i])
    return sorted(segmentation, key=lambda x: x[0])
