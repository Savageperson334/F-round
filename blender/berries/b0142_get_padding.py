# get_padding
#
# Copied verbatim from https://github.com/ChristianBergler/ANIMAL-SPOT
#   file ANIMAL-SPOT/models/utils.py, line 10
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Animal acoustics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def get_padding(kernel_size):
    if isinstance(kernel_size, int):
        return kernel_size // 2
    else:
        return tuple(s // 2 for s in kernel_size)
