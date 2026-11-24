# edit_distance
#
# Copied verbatim from https://github.com/isi-vista/VistaOCR
#   file src/textutils.py, line 264
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def edit_distance(A, B):
    # If both strings are empty, edit distance is 0                                                                               
    if len(A) == 0 and len(B) == 0:
        return 0
    # If one or the other is empty, then edit distance is length of the other one                                                 
    if len(A) == 0 or len(B) == 0:
        return len(A) + len(B)

    # Otherwise have to actually compute it the hard way :)                                                                       
    dist_matrix = np.zeros((len(A)+1, len(B)+1))
    for i in range(len(A)+1):
        dist_matrix[i, 0] = i
    for j in range(len(B)+1):
        dist_matrix[0, j] = j

    for i in range(1,len(A)+1):
        for j in range(1,len(B)+1):
            if A[i-1] == B[j-1]:
                dist_matrix[i,j] = dist_matrix[i-1,j-1]
            else:
                dist_matrix[i, j] = 1 + min(dist_matrix[i, j - 1], dist_matrix[i - 1, j],
                                            dist_matrix[i - 1, j - 1])

    return dist_matrix[-1, -1]
