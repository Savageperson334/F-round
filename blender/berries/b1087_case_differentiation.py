# case_differentiation
#
# Copied verbatim from https://github.com/anshdavid/Procedural-City-Generation
#   file procedural_city_generation/roadmap/growth_rules/radial.py, line 66
#   licence (as GitHub reports it): MPL-2.0   see ../licenses/
#   catalogue shelf: Procedural and generated worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math
import numpy as np


def case_differentiation(v1, v2):
    """
    Finds out if the angle between two vectors is closest to 0, 90, 180, 270 degrees.
    Returns the angle in degrees to which the first vector has to be rotated
    in order to be either parrallel or perpendicular to the second vector.

    Parameters
    ----------
    v1 : np.ndarray(2, )
    v2 : np.ndarray(2, )

    Returns
    -------
    float
    """

    alpha1=math.atan2(v1[1], v1[0])
    alpha2=math.atan2(v2[1], v2[0])
    alpha= (alpha2-alpha1)*180/np.pi
    if alpha<0:
        alpha+=360
    if (alpha >=45 and alpha <90) or (alpha>=225 and alpha<270):
        alpha-=90
    elif (alpha >=90   and alpha <135  ) or (alpha>=270    and alpha < 315  ):
        alpha+=90

    elif (alpha>=135 and alpha <225):
        alpha-=180

    return alpha
