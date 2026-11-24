# single_val_format
#
# Copied verbatim from https://github.com/timpol/DQPB
#   file dqpb/util.py, line 105
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


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


def single_val_format(v, sf=4, plims=(-3,5)):
    """
    Parameters
    -----------
    sf : int
        Number of significant figures to display (only applies to decimal
        component)
    """

    sf = int(sf)
    if sf < 0:
        raise ValueError("can't have a negative or 0 number of significant figures")
    s = -1 if v < 0 else 1
    v = v * s

    if v == 0.:
        return print_format_str(sf)

    p = math.floor(math.log10(v))

    if 10 ** plims[0] < s * v < 10 ** plims[1]:
        if p >= (sf + 1):
            d = 0
        else:
            d = sf - p - 1
        return print_format_str(d)

    else:
        return print_format_str(sf-1 if sf > 1 else 1, sci=True)
