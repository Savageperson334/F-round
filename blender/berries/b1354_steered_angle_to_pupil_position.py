# steered_angle_to_pupil_position
#
# Copied verbatim from https://github.com/choisuyeon/sawh
#   file utils/utils.py, line 197
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Optical computing and holograms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def steered_angle_to_pupil_position(f, steered_angle):
    """Convert steered_angle to pupil-plane position using eyepiece focal length."""
    if steered_angle is None:
        return (0.0, 0.0)
    return tuple(np.tan(a) * f for a in steered_angle)
