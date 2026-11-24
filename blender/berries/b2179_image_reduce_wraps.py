# image_reduce_wraps
#
# Copied verbatim from https://github.com/holodyne/slmsuite
#   file slmsuite/holography/analysis/__init__.py, line 1854
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Optical computing and holograms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def image_reduce_wraps(phase_image, mask=None, steps=10, plot=0):
    """
    Reduce the number of phase wraps in the image by adding a global offset.

    Parameters
    ----------
    phase_image : np.ndarray
        The phase image to be offset.
    mask : np.ndarray OR None
        If provided, the mask will weight the significance of the phase wraps.
        This can be the amplitude image, such that fewer wraps appear where there is
        light.
    steps : int
        The number of steps to try for the phase offset.
    plot : int OR bool
        Whether to enable debug plots.

    Returns
    -------
    np.ndarray
        A phase image with the offset applied.
    """
    # Initialize such that the first iteration is always the best.
    fom_min = np.inf
    result = None

    # Loop through all offsets.
    for phi in range(steps):
        shift = phi * 2 * np.pi / steps
        phase_shifted = np.mod(phase_image + shift, 2 * np.pi)

        # Find where the phase wraps.
        wrapping = (
            np.abs(np.gradient(phase_shifted, axis=1)) + np.abs(np.gradient(phase_shifted, axis=0))
        ) > np.pi

        if mask is not None:
            wrapping = wrapping * mask

        # Sum the total cut area, potentially weighted by the mask.
        fom = np.sum(wrapping)

        if fom < fom_min:
            fom_min = fom
            result = phase_shifted

    # Shift the chosen winner to either end of the 0 -> 2pi range.
    if result is not None:
        min = np.nanmin(result)
        mean = np.nanmean(result)
        max = np.nanmax(result)

        if mean - min < max - mean:
            result = result - min
        else:
            result = result - (max - 2 * np.pi)

        result = np.mod(result, 2 * np.pi)

    return result
