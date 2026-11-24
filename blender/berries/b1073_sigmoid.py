# sigmoid
#
# Copied verbatim from https://github.com/angrysky56/mycelium_network
#   file examples/archive/hybrid_example_fixed.py, line 28
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Animal surveillance, plants and living-world computation
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def sigmoid(x: float) -> float:
    """Numerically stable sigmoid function."""
    if x >= 0:
        z = math.exp(-x)
        return 1 / (1 + z)
    else:
        z = math.exp(x)
        return z / (1 + z)
