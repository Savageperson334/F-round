# smooth
#
# Copied verbatim from https://github.com/SarthakJariwala/Python_GUI_apps
#   file PythonGUI_apps/Lifetime_analysis/read_ph_phd.py, line 40
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def smooth(curve, boxwidth):
    sm_curve = np.convolve(curve, np.ones(boxwidth)/boxwidth, mode="same")
    return sm_curve
