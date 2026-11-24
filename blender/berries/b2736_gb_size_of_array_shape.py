# gb_size_of_array_shape
#
# Copied verbatim from https://github.com/mesoSPIM/mesoSPIM-control
#   file mesoSPIM/src/utils/utility_functions.py, line 94
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Microscopy & small worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def gb_size_of_array_shape(shape):
        '''Given a tuple of array shape, return the size in GB of a uint16 array.

        Args:
            shape (tuple[int]): Array dimensions, e.g. ``(100, 2048, 2048)``.

        Returns:
            float: Size in gibibytes (GiB).
        '''
        for idx,ii in enumerate(shape):
            if idx == 0:
                total = ii
            else:
                total *= ii
        total = total * 16 / 8
        return total / 1024**3
