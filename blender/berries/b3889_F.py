# F
#
# Copied verbatim from https://github.com/volkanozsarac/OSW-6ICEES
#   notebook 2. Python.ipynb (its code cells joined in order; line 610 of those)
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def F(x):
    value = x*x - 3.
    derivative = 2*x
    return (value, derivative)
