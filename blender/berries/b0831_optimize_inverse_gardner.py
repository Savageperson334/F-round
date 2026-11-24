# optimize_inverse_gardner
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/petrophysics/petrophysics.py, line 183
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


def optimize_inverse_gardner(rho, alpha, beta):
     """ Wrapper function to pass inverse_gardner to scipy.curve_fit
     to get optimal alpha and beta parameters

     Matteo Niccoli and Volodymyr Vragov, October 2018

     Args:
         rho(ndarray): Density.
         alpha (float): The factor.
         beta (float): The exponent.

     Returns:
         inverse_gardner: this is passed to scipy.curve_fit as, for example:
         popt_synt, pcov = scipy.curve_fit(optimize_inverse_gardner, rho, vp)
         For a full example, please read:
         mycarta.wordpress.com/2018/10/28/geophysics-python-sprint-2018-day-2-and-beyond-part-i
     """
     return inverse_gardner(rho, alpha=alpha, beta=beta)
