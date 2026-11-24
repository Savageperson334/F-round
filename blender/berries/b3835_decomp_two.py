# decomp_two
#
# Copied verbatim from https://github.com/trichter/rf
#   file rf/harmonics.py, line 136
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def decomp_two(baz, azim=0, scalars=(3, 0.3)):
    """ Build jacobian for harmonic decomposition with two components of RFs.

    :param baz: array of back azimuths for RFs in degrees
    :param azim: azimuth along which to decompose the RFs.
        This can be used with some kind of optimization minimize components
    :param scalars: scalar multipliers for R/Q and T constant terms.
        Park and Levin (2016) recommend 3 and 0.3 to bias toward radial component
        conversions, especially for datasets with patchy back-azimuthal coverage.
        (1,1) would weight Q/R and T equally in the regression.
    :return: jacobian matrix as np.ndarray, 10xN where N is the time series length
    """
    jacr = np.array([scalars[0]*np.ones(len(baz)),
                     np.cos(np.radians(baz-azim)),
                     np.sin(np.radians(baz-azim)),
                     np.cos(2*np.radians(baz-azim)),
                     np.sin(2*np.radians(baz-azim)),
                     np.zeros(len(baz)),
                     np.cos(np.radians(baz-azim)),
                     np.sin(np.radians(baz-azim)),
                     np.cos(2*np.radians(baz-azim)),
                     np.sin(2*np.radians(baz-azim))])
    jact = np.array([np.zeros(len(baz)),
                     -np.sin(np.radians(baz-azim)),
                     np.cos(np.radians(baz-azim)),
                     -np.sin(2*np.radians(baz-azim)),
                     np.cos(2*np.radians(baz-azim)),
                     scalars[1]*np.ones(len(baz)),
                     np.sin(np.radians(baz-azim)),
                     -np.cos(np.radians(baz-azim)),
                     np.sin(2*np.radians(baz-azim)),
                     -np.cos(2*np.radians(baz-azim))])
    jac = np.hstack((jacr, jact))
    return jac.T
