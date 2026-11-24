# normalize
#
# Copied verbatim from https://github.com/ideoforms/isobar
#   file isobar/util.py, line 22
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Sound sonification
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def normalize(array: list[float]) -> list[float]:
    """
    Normalise an array to sum to 1.0.
    """
    if sum(array) == 0:
        return array
    return [float(n) / sum(array) for n in array]
