# bipolar_diverge
#
# Copied verbatim from https://github.com/ideoforms/isobar
#   file isobar/util.py, line 298
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Sound sonification
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def bipolar_diverge(maximum: int) -> list[int]:
    """
    Returns [0, 1, -1, ...., maximum, -maximum ]
    """
    sequence = list(sum(list(zip(list(range(maximum + 1)), list(range(0, -maximum - 1, -1)))), ()))
    sequence.pop(0)
    return sequence
