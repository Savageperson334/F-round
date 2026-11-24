# texture_from_generator
#
# Copied verbatim from https://github.com/paulgb/penkit
#   file penkit/turtle.py, line 92
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Plotters & drawing machines
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def texture_from_generator(generator):
    """Convert a generator into a texture.

    Args:
        generator (generator): a generator of coordinate pairs

    Returns:
        texture: A texture.
    """
    return np.array(list(zip(*list(generator))))
