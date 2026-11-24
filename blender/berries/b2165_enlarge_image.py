# enlarge_image
#
# Copied verbatim from https://github.com/hila-chefer/Transformer-Explainability
#   file utils/render.py, line 35
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def enlarge_image(img, scaling=3):
    '''
    Enlarges a given input matrix by replicating each pixel value scaling times in horizontal and vertical direction.

    Parameters
    ----------

    img : numpy.ndarray
        array of shape [H x W] OR [H x W x D]

    scaling : int
        positive integer value > 0

    Returns
    -------

    out : numpy.ndarray
        two-dimensional array of shape [scaling*H x scaling*W]
        OR
        three-dimensional array of shape [scaling*H x scaling*W x D]
        depending on the dimensionality of the input
    '''

    if scaling < 1 or not isinstance(scaling, int):
        print('scaling factor needs to be an int >= 1')

    if len(img.shape) == 2:
        H, W = img.shape

        out = np.zeros((scaling * H, scaling * W))
        for h in range(H):
            fh = scaling * h
            for w in range(W):
                fw = scaling * w
                out[fh:fh + scaling, fw:fw + scaling] = img[h, w]

    elif len(img.shape) == 3:
        H, W, D = img.shape

        out = np.zeros((scaling * H, scaling * W, D))
        for h in range(H):
            fh = scaling * h
            for w in range(W):
                fw = scaling * w
                out[fh:fh + scaling, fw:fw + scaling, :] = img[h, w, :]

    return out
