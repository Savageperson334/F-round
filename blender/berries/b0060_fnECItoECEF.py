# fnECItoECEF
#
# Copied verbatim from https://github.com/AshivDhondea/Satellite_Ground_Track_Plotting_Python
#   file AstroFunctions.py, line 52
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np
import math


def fnRotate3(alpha_rad):
    T = np.array([[ math.cos(alpha_rad),math.sin(alpha_rad),0], 
                  [-math.sin(alpha_rad),math.cos(alpha_rad),0],
                  [                 0,                0,1]],dtype=np.float64);
    return T


def fnECItoECEF(ECI,theta):
    ECEF = np.zeros([3],dtype=np.float64);
    # Rotating the ECI vector into the ECEF frame via the GST angle about the Z-axis
    ECEF = np.dot(fnRotate3(theta),ECI);
    return ECEF
