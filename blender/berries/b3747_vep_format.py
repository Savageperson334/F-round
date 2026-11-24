# vep_format
#
# Copied verbatim from https://github.com/timpol/DQPB
#   file dqpb/util.py, line 66
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math
import numpy as np


def print_format_str(d_places, sci=False):
    """
    """
    d_places = int(d_places)

    if not sci:
        bs = "#,##0"
        if d_places > 0:
            fs = bs + '.' + d_places * '0'
        else:
            fs = bs
    else:
        bs1 = "0.0"
        bs2 = "E+00"
        if d_places > 0:
            fs = bs1 + (d_places - 1) * "0" + bs2
        else:
            fs = bs1 + bs2

    return fs


def vep_format(v, e, plims=(-3,5)):
    """
    Use order of magnitude of error to determine number of decimal places to
    show for a numeric result, given error is shown to two decimal places.
    """

    if not np.all(np.isfinite((v, e))):
        return "#.00", "#.00"

    s = -1 if v < 0 else 1  # get sign for later
    v = v * s  # Convert to positive value
    e = abs(e)  # Error should always be positive, but just in case.

    # Find number of decimal places required from order of magnitude. E.g.
    # >0 -> 0 decimal places for value and error
    # 0 -> 1
    # -1 -> 2
    # -2 -> 3

    p = math.floor(math.log10(e))
    # If number is within power limits, do not use scientific notation
    if 10 ** plims[0] < v * s < 10 ** plims[1]:
        # find number of decimal places
        if p > 1:
            d = 0
        else:
            d = -1 * p + 1
        fs = print_format_str(d)
        # Use same format string for value and error
        return fs, fs
    else:
        pv = math.floor(math.log10(v))
        q = pv - p
        q = q + 1 if q > 0 else 1
        fse = print_format_str(1, sci=True)
        fsv = print_format_str(q, sci=True)
        return fsv, fse
