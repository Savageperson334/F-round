# vs2vprho
#
# Copied verbatim from https://github.com/xumi1993/seispy
#   file seispy/utils.py, line 10
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def vs2vprho(vs):
    """
    Calculate vp and rho from vs using Brocher (2005) formula.

    :param vs: vs in km/s
    :type vs: float or np.ndarray

    :return: vp and rho in km/s and g/cm^3
    :rtype: tuple
    """
    vp = 0.9409 + 2.0947*vs - 0.8206*vs**2 + 0.2683*vs**3 - 0.0251*vs**4
    rho = 1.6612*vp - 0.4721*vp**2 + 0.0671*vp**3 - 0.0043*vp**4 + 0.000106*vp**5
    # vs = 0.7858 - 1.2344*vp + 0.7949*vp**2 - 0.1238*vp**3 + 0.0064*vp**4
    return vp, rho
