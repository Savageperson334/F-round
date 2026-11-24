# decomp_one
#
# Copied verbatim from https://github.com/trichter/rf
#   file rf/harmonics.py, line 172
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def decomp_one(baz, azim=0):
    """ Build jacobian for harmonic decomposition for one RF component.

    :param baz: array of back azimuths for RFs in degrees
    :param azim: azimuth along which to decompose the RFs.
        This can be used with some kind of optimization minimize components
    :return: jacobian matrix as np.ndarray, 5xN where N is time series length
    """
    jac = np.array([np.ones(len(baz)),
                    np.cos(np.radians(baz-azim)),
                    np.sin(np.radians(baz-azim)),
                    np.cos(2*np.radians(baz-azim)),
                    np.sin(2*np.radians(baz-azim))])
    return jac.T
