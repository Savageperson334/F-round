# calcfreqscale
#
# Copied verbatim from https://github.com/Ma-Weber/Tutorial-Deconvolution
#   notebook TutorialFinal.ipynb (its code cells joined in order; line 27 of those)
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Ocean hydrophones and acoustic ecology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def calcfreqscale(timeseries,sign2 = 1):
    """Calculates the appropriate time scale for a given (equidistant) time series
    TODO: Add case for Complex GUM_DFT

    Parameters
    ----------
        timeseries: ndarray
            strictly increasing and equidistant steps of the sampling time, max- and min-value is used for calculation
        sign2: integer (optional)
            sign for sin part frequencies, allows to be negative for plotting
            1 gives positive frequencies fitting to GUM_DFT data (default)
            0 gives only first half
            -1 sin part is negative, usable for easy plotting


    Returns
    -------
        f: ndarray
            frequencies matching the result of GUM_DFT if sign2 has the default value of 1

    """
    n = np.size(timeseries)
    if sign2 < 0:
        sign = -1
    else:
        sign = 1

    fmax = 1/((np.max(timeseries)-np.min(timeseries))*n/(n-1))*(n-1)

    f = np.linspace(0,fmax,n)

    f2 = np.hstack((f[0:int(n/2.+1)],sign*f[0:int(n/2+1)]))
    if sign2 == 0:
        f2 = f[0:int(n/2.+1)]

    return f2
