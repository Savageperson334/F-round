# is_diagonal
#
# Copied verbatim from https://github.com/CassGut/Kinova-Gen-3-Robotic-Arm-Pick-and-Place-Controller-Tutorial
#   notebook Part 2/4_0_Numerical_Inverse_Kinematics.ipynb (its code cells joined in order; line 395 of those)
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Robots and tactile mechanisms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def is_diagonal(matrix):
    # Check if the matrix is square
    if len(matrix) != len(matrix[0]):
        return False

    # Iterate through rows and columns
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # If an off-diagonal element is not zero, return False
            if i != j and matrix[i][j] !=  0:
                return False

    # If no off-diagonal elements are non-zero, return True
    return True
