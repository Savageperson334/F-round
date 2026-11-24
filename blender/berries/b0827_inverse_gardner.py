# inverse_gardner
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/petrophysics/petrophysics.py, line 33
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def inverse_gardner(rho, alpha=310, beta=0.25, fps=False):
    """
    Computes Gardner's density prediction from P-wave velocity.

    Args:
        rho (ndarray): Density in kg/m^3.
        alpha (float): The factor, 310 for m/s and 230 for fps.
        beta (float): The exponent, usually 0.25.
        fps (bool): Set to true for FPS and the equation will use the typical
            value for alpha. Overrides value for alpha, so if you want to use
            your own alpha, regardless of units, set this to False.

    Returns:
        ndarray: Vp estimate in m/s.
    """
    alpha = 230 if fps else alpha
    exponent = 1 / beta
    factor = 1 / alpha**exponent
    return factor * rho**exponent
