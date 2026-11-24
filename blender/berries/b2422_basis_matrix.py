# basis_matrix
#
# Copied verbatim from https://github.com/jesserobertson/earthchem-pyclient
#   file earthchem/transform/utilities.py, line 37
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def basis_matrix(n_dimensions):
    """
    Return the ILR basis matrix for the given number of dimensions

    Parameters:
        n_dimensions - the number of dimensions

    Returns:
        the basis matrix V for the ILR
    """
    D = n_dimensions
    Psi = np.zeros((D - 1, D))
    for i in range(1, D):
        for j in range(1, D + 1):
            if j <= D - i:
                Psi[i - 1, j - 1] = np.sqrt(1 / ((D - i) * (D - i + 1)))
            elif j == D - i + 1:
                Psi[i - 1, j - 1] = -np.sqrt((D - i) / (D - i + 1)) 
    return Psi
