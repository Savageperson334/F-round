# residual
#
# Copied verbatim from https://github.com/cbassa/stvid
#   file stvid/extract.py, line 23
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def model(a, nx, ny):
    x, y = np.meshgrid(np.arange(nx), np.arange(ny))
    dx, dy = (x - a[0]) / a[2], (y - a[1]) / a[2]
    arg = -0.5 * (dx**2 + dy**2)
    return a[3] * np.exp(arg) + a[4]


def residual(a, img):
    ny, nx = img.shape
    mod = model(a, nx, ny)
    return (img - mod).ravel()
