# clip
#
# Copied verbatim from https://github.com/ideoforms/isobar
#   file isobar/util.py, line 284
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Sound sonification
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def clip(value: float, minimum: float, maximum: float) -> float:
    """
    Clip a value to a range.

    Args:
        value: The value
        minimum: The lower bound of the range
        maximum: The upper bound of the range

    Returns:
        The clipped value.
    """
    return max(minimum, min(value, maximum))
