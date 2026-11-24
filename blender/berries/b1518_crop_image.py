# crop_image
#
# Copied verbatim from https://github.com/computational-imaging/neural-3d-holography
#   file utils.py, line 114
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Optical computing and holograms
#   the same function also appears in: computational-imaging/time-multiplexed-neural-holography
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def crop_image(field, target_shape, pytorch=True, stacked_complex=True, lf=False):
    """Crops a 2D field, see pad_image() for details

    No cropping is done if target_shape is already smaller than field
    """
    if target_shape is None:
        return field

    if lf:
        size_diff = np.array(field.shape[-4:-2]) - np.array(target_shape)
        odd_dim = np.array(field.shape[-4:-2]) % 2
    else:
        if pytorch:
            if stacked_complex:
                size_diff = np.array(field.shape[-3:-1]) - np.array(target_shape)
                odd_dim = np.array(field.shape[-3:-1]) % 2
            else:
                size_diff = np.array(field.shape[-2:]) - np.array(target_shape)
                odd_dim = np.array(field.shape[-2:]) % 2
        else:
            size_diff = np.array(field.shape[-2:]) - np.array(target_shape)
            odd_dim = np.array(field.shape[-2:]) % 2

    # crop dimensions that need to decrease in size
    if (size_diff > 0).any():
        crop_total = np.maximum(size_diff, 0)
        crop_front = (crop_total + 1 - odd_dim) // 2
        crop_end = (crop_total + odd_dim) // 2

        crop_slices = [slice(int(f), int(-e) if e else None)
                       for f, e in zip(crop_front, crop_end)]
        if lf:
            return field[(..., *crop_slices, slice(None), slice(None))]
        else:
            if pytorch and stacked_complex:
                return field[(..., *crop_slices, slice(None))]
            else:
                return field[(..., *crop_slices)]
    else:
        return field
