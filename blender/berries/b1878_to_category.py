# to_category
#
# Copied verbatim from https://github.com/ferencberes/LNTrafficSimulator
#   notebook notebooks/Examples.ipynb (its code cells joined in order; line 175 of those)
#   licence (as GitHub reports it): CC0-1.0   see ../licenses/
#   catalogue shelf: Public transport and city motion
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def to_category(x):
    if x > 100:
        return 3
    elif x > 10:
        return 2
    elif x > 0:
        return 1
    else:
        return 0
