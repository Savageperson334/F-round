# to_polar
#
# Copied verbatim from https://github.com/XiaokangLiuCUG/DeepMorph
#   file ammonoids_landmarks.py, line 150
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Laboratories, geochemistry, chemistry and microscopes
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from math import atan2


def to_polar(vector, centered_x, centered_y):   #Cartesian coordinates to polar coordinates
    x, y = vector[0]-centered_x, vector[1]-centered_y
    angle = atan2(y,x)
    #return (length(vector), angle)
    return angle
