# vector_to_line
#
# Copied verbatim from https://github.com/morganjwilliams/exploratory-geochemistry
#   file src/plotting_tools.py, line 104
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def vector_to_line(mu:np.array,
                   vector:np.array,
                   variance:float,
                   spans: int=4,
                   expand: int=10):
    """
    Creates an array of points representing a line along a vector - typically
    for principal component analysis.

    Modified after Jake VanderPlas' Python Data Science Handbook
    https://jakevdp.github.io/PythonDataScienceHandbook/05.09-principal-component-analysis.html
    """
    length = np.sqrt(variance)
    parts = np.linspace(-spans, spans, expand * 2 * spans + 1)
    line =  length * np.dot(parts[:, np.newaxis], vector[np.newaxis, :]) + mu
    line =  length * parts.reshape(parts.shape[0], 1) * vector + mu
    return line
