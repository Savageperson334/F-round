# safe_log
#
# Copied verbatim from https://github.com/fatiando/fatiando
#   file fatiando/gravmag/_prism_numpy.py, line 26
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from numpy import log


def safe_log(x):
    """
    Return 0 for log(0) because the limits in the formula terms tend to 0
    (see Nagy et al., 2000)
    """
    res = log(x)
    res[x == 0] = 0
    return res
