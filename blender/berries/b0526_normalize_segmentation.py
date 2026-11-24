# normalize_segmentation
#
# Copied verbatim from https://github.com/MartinThoma/hwrt
#   file hwrt/segmentation/segmentation.py, line 993
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def normalize_segmentation(seg):
    """
    Bring the segmentation into order.

    Parameters
    ----------
    seg : list of lists of ints

    Returns
    -------
    seg : list of lists of ints

    Examples
    --------
    >>> normalize_segmentation([[5, 2], [1, 4, 3]])
    [[1, 3, 4], [2, 5]]
    """
    return sorted(sorted(el) for el in seg)
