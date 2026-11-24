# image_ellipticity_angle
#
# Copied verbatim from https://github.com/holodyne/slmsuite
#   file slmsuite/holography/analysis/__init__.py, line 1002
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Optical computing and holograms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def image_ellipticity_angle(variances):
    r"""
    Given the output of :meth:`image_variances()`,
    return the rotation angle of the scaled basis for each moment triplet.
    This is the angle between the :math:`x` axis and the
    major axis (large eigenvalue axis).

    Parameters
    ----------
    variances : numpy.ndarray
        The output of :meth:`image_variances()`. Shape ``(3, image_count)``.

    Returns
    -------
    numpy.ndarray
        Array of angles for the given moments.
        For highly circular spots, this angle is not meaningful, and dominated by
        experimental noise.
        For perfectly circular spots, zero is returned.
        Shape ``(image_count,)``.
    """
    m20 = variances[0, :]
    m02 = variances[1, :]
    m11 = variances[2, :]

    # Major-axis orientation of the [[m20, m11], [m11, m02]] covariance.
    return 0.5 * np.arctan2(2 * m11, m20 - m02)
