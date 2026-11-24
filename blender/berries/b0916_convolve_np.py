# convolve_np
#
# Copied verbatim from https://github.com/agilescientific/in-bruges
#   notebook notebooks/n-dimensional_convolution.ipynb (its code cells joined in order; line 297 of those)
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def convolve_np(reflectivity, wavelet, verbose=True):
    """
    Convolve reflectivity with wavelet using np.apply_along_axis under the hood.

    For now, this seems to be slightly slower than the approach using map, above.
    I don't know why, because they were very similar in the tests above.
    """
    # Compute the target shape of the final synthetic.
    outshape = wavelet.shape[:-1] + reflectivity.shape

    # Force wavelet and reflectivity to both be 2D.
    bank = np.atleast_2d(wavelet)   
    reflectivity_2d = reflectivity.reshape((-1, reflectivity.shape[-1]))

    # Compute synthetic, which will always be 3D.
    syn = np.array([np.apply_along_axis(lambda tr: np.convolve(tr, w, mode='same'),
                                        arr=reflectivity_2d,
                                        axis=-1)
                    for w in bank])

    # Show the shapes of the data we're handling.
    if verbose:
        print(reflectivity.shape, ' * ', wavelet.shape, ' -> ', outshape)

    return syn.reshape(outshape)
