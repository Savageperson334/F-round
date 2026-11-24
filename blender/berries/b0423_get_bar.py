# get_bar
#
# Copied verbatim from https://github.com/KMFleischer/PyEarthScience
#   file Transition_examples_NCL_to_PyNGL/xy/TRANS_bar_chart.py, line 45
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def get_bar(x,y,dx,ymin,bar_width_perc=0.6):
	dxp  =  (dx * bar_width_perc)/2.
	xbar =  np.array([x-dxp, x+dxp, x+dxp, x-dxp, x-dxp])
	ybar =  np.array([ ymin, ymin,    y,    y, ymin])
	return xbar,ybar
