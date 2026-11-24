# sigmoid_derivative
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/vector/__init__.py, line 3162
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def sigmoid_derivative(y):
    """ Backward propagation activation function derivative.
    """
    #return y * (1.0 - y)
    return 1.0 - y * y
