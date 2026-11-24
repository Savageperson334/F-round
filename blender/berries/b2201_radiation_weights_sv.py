# radiation_weights_sv
#
# Copied verbatim from https://github.com/hvasbath/beat
#   file beat/heart.py, line 3915
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def radiation_weights_sv(takeoff_angles, azimuths):
    """
    Station dependent propagation coefficients for SV waves

    Notes
    -----
    Pugh et al., A Bayesian method for microseismic source inversion, 2016, GJI
    Appendix A
    """

    st = num.sin(takeoff_angles)
    ct = num.cos(takeoff_angles)
    sct = st * ct

    ct2 = num.cos(2 * takeoff_angles)

    ca = num.cos(azimuths)
    sa = num.sin(azimuths)
    return num.array(
        [sct * ca**2, sct * sa**2, -sct, 2 * sct * sa * ca, ct2 * ca, ct2 * sa]
    )
