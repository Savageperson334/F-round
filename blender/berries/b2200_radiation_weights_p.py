# radiation_weights_p
#
# Copied verbatim from https://github.com/hvasbath/beat
#   file beat/heart.py, line 3891
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def radiation_weights_p(takeoff_angles, azimuths):
    """
    Station dependent propagation coefficients for P waves

    Notes
    -----
    Pugh et al., A Bayesian method for microseismic source inversion, 2016, GJI
    Appendix A
    """

    st = num.sin(takeoff_angles)
    ct = num.cos(takeoff_angles)
    stp2 = st**2
    st2 = 2 * st * ct  # num.sin(2 * takeoff_angles)

    ca = num.cos(azimuths)
    sa = num.sin(azimuths)
    sa2 = 2 * ca * sa  # num.sin(2 * azimuths)

    return num.array(
        [stp2 * ca**2, stp2 * sa**2, ct**2, stp2 * sa2, st2 * ca, st2 * sa]
    )
