# fnCarts_to_LatLon
#
# Copied verbatim from https://github.com/AshivDhondea/Satellite_Ground_Track_Plotting_Python
#   file AstroFunctions.py, line 89
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math
import numpy as np


def fnCarts_to_LatLon(R):
    """
    function which converts ECEF position vectors to latitude and longitude
    Based on rvtolatlong.m in Richard Rieber's orbital library on mathwork.com

    Note that this is only suitable for groundtrack visualization, not rigorous 
    calculations.
    Date: 18 September 2016
    """
    r_delta = np.linalg.norm(R[0:1]);
    sinA = R[1]/r_delta;
    cosA = R[0]/r_delta;

    Lon = math.atan2(sinA,cosA);

    if Lon < -math.pi:
        Lon = Lon + 2*math.pi;

    Lat = math.asin(R[2]/np.linalg.norm(R));
    return Lat,Lon
