# cos_matrix_multiplication
#
# Copied verbatim from https://github.com/HendrikStrobelt/LSTMVis
#   file lstmdata/helper_functions.py, line 74
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def cos_matrix_multiplication(matrix, vector, matrix_norms=None):
    """Calculating pairwise cosine distance using matrix vector multiplication.

    :param matrix: matrix
    :param vector: vector
    :param matrix_norms: pre-computed matrix norms
    """
    # print matrix.shape
    # print vector.shape

    if not matrix_norms:
        matrix_norms = np.linalg.norm(matrix, axis=1)

    dotted = matrix.dot(vector)

    vector_norm = np.linalg.norm(vector)
    matrix_vector_norms = np.multiply(matrix_norms, vector_norm)
    neighbors = np.divide(dotted, matrix_vector_norms)
    return neighbors
