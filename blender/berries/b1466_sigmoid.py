# sigmoid
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/vector/__init__.py, line 3155
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from math import tanh


def sigmoid(x):
    """ Forward propagation activation function.
    """
    #return 1.0 / (1.0 + math.exp(-x))
    return tanh(x)
