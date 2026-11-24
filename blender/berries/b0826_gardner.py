# gardner
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/petrophysics/petrophysics.py, line 14
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def gardner(vp, alpha=310, beta=0.25, fps=False):
    """
    Computes Gardner's density prediction from P-wave velocity.

    Args:
        vp (ndarray): P-wave velocity in m/s.
        alpha (float): The factor, 310 for m/s and 230 for ft/s.
        beta (float): The exponent, usually 0.25.
        fps (bool): Set to true for FPS and the equation will use the typical
            value for alpha. Overrides value for alpha, so if you want to use
            you own alpha, regardless of units, set this to False.

    Returns:
        ndarray: RHOB estimate in :math:`kg/m^3`.
    """
    alpha = 230 if fps else alpha
    return alpha * vp ** beta
