# xy
#
# Copied verbatim from https://github.com/fogleman/axi
#   file examples/rush.py, line 73
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Plotters & drawing machines
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def xy(i):
    x = i % 6
    y = i // 6
    return (x, y)
