# zoom
#
# Copied verbatim from https://github.com/glumpy/glumpy
#   file glumpy/graphics/text/sdf_font.py, line 41
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def bilinear_interpolate(im, x, y):
    """ By Alex Flint on StackOverflow """

    x = np.asarray(x)
    y = np.asarray(y)

    x0 = np.floor(x).astype(int)
    x1 = x0 + 1
    y0 = np.floor(y).astype(int)
    y1 = y0 + 1

    x0 = np.clip(x0, 0, im.shape[1]-1);
    x1 = np.clip(x1, 0, im.shape[1]-1);
    y0 = np.clip(y0, 0, im.shape[0]-1);
    y1 = np.clip(y1, 0, im.shape[0]-1);

    Ia = im[ y0, x0 ]
    Ib = im[ y1, x0 ]
    Ic = im[ y0, x1 ]
    Id = im[ y1, x1 ]

    wa = (x1-x) * (y1-y)
    wb = (x1-x) * (y-y0)
    wc = (x-x0) * (y1-y)
    wd = (x-x0) * (y-y0)

    return wa*Ia + wb*Ib + wc*Ic + wd*Id


def zoom(Z, ratio):
    """ Bilinear image zoom """

    nrows, ncols = Z.shape
    x,y = np.meshgrid(np.linspace(0, ncols, int(round(ratio*ncols)), endpoint=False),
                      np.linspace(0, nrows, int(round(ratio*nrows)), endpoint=False))
    return bilinear_interpolate(Z, x, y)
