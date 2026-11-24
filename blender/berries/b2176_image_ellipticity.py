# image_ellipticity
#
# Copied verbatim from https://github.com/holodyne/slmsuite
#   file slmsuite/holography/analysis/__init__.py, line 911
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Optical computing and holograms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def image_ellipticity(variances):
    r"""
    Given the output of :meth:`image_variances()`,
    return a measure of spot ellipticity for each moment triplet.
    The output of :meth:`image_variances()` contains the moments :math:`M_{20}`,
    :math:`M_{02}`, and :math:`M_{11}`. These terms make up a :math:`2 \times 2` matrix,
    which is equivalent to a rotated elliptical scaling according to the eigenvalues
    :math:`\lambda_+` and :math:`\lambda_-` and some rotation matrix :math:`R(\phi)`.

    .. math::   \begin{bmatrix}
                    M_{20} & M_{11} \\
                    M_{11} & M_{02} \\
                \end{bmatrix}
                =
                R(-\phi)
                \begin{bmatrix}
                    \lambda_+ & 0 \\
                    0 & \lambda_- \\
                \end{bmatrix}
                R(\phi).

    We use this knowledge, along with tricks for eigenvalue calculations on
    :math:`2 \times 2` matrices, to build up a metric for ellipticity:

    .. math:: \mathcal{E} = 1 - \frac{\lambda_-}{\lambda_+}.

    Notice that

    - when :math:`\lambda_+ = \lambda_-` (isotropic scaling), the metric is zero and
    - when :math:`\lambda_- = 0` (flattened to a line), the metric is unity.

    Parameters
    ----------
    variances : numpy.ndarray
        The output of :meth:`image_variances()`. Shape ``(3, image_count)``.

    Returns
    -------
    numpy.ndarray
        Array of ellipticities for the given moments in an array of shape ``(image_count,)``.
        ``nan`` where :math:`\lambda_+ = 0`, such as for an all-zero image.
    """
    m20 = variances[0, :]
    m02 = variances[1, :]
    m11 = variances[2, :]

    # We can use a trick for eigenvalue calculations of 2x2 matrices to avoid
    # more complicated calculations.
    half_trace = (m20 + m02) / 2
    determinant = m20 * m02 - m11 * m11

    eig_half_difference = np.sqrt(np.maximum(np.square(half_trace) - determinant, 0))

    eig_plus = half_trace + eig_half_difference
    eig_minus = half_trace - eig_half_difference

    # eig_plus == 0 for an all-zero / uniform image; return nan there instead of dividing.
    ratio = np.divide(
        eig_minus,
        eig_plus,
        out=np.full_like(eig_plus, np.nan, dtype=float),
        where=eig_plus != 0,
    )
    return 1 - ratio
