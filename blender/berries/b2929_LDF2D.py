# LDF2D
#
# Copied verbatim from https://github.com/nu-radio/radiotools
#   file radiotools/coreas/generate_coreas_sim.py, line 579
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sky, weather, satellites and unobservable phenomena
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def LDF2D(x, y, zenith, dxmax, cx=0, cy=0):
    c0 = 0.41
    c3 = 16.25
    c4 = 0.0079
    if zenith < np.deg2rad(10):
        c1 = 8.
        c2 = -21.2
    elif zenith < np.deg2rad(20):
        c1 = 10.
        c2 = -23.1
    elif zenith < np.deg2rad(30):
        c1 = 12.
        c2 = -25.5
    elif zenith < np.deg2rad(40):
        c1 = 20.
        c2 = -32.
    elif zenith < np.deg2rad(50):
        c1 = 25.1
        c2 = -34.5
    elif zenith < np.deg2rad(55):
        c1 = 27.3
        c2 = -9.8
        c0 = 0.46
    elif zenith >= np.deg2rad(55):
        c1 = 27.3
        c2 = -9.8
        c0 = 0.71
    # dxmax = hp.get_distance_xmax(xmax, zenith, observation_level)
    s1 = 37.7 - 0.006 * dxmax + 5.5e-4 * dxmax ** 2 - 3.7e-7 * dxmax ** 3
    s2 = 26.9 - 0.041 * dxmax + 2e-4 * dxmax ** 2
    A = 1.  # only relative scaling is important
    p1 = A * np.exp(-((x - cx + c1) ** 2 + (y - cy) ** 2) / s1 ** 2)
    p2 = A * c0 * np.exp(-((x - cx + c2) ** 2 + (y - cy) ** 2) / (s2) ** 2)
    return p1 - p2
