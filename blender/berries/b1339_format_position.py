# format_position
#
# Copied verbatim from https://github.com/cbassa/stvid
#   file stvid/extract.py, line 149
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def format_position(ra, de):
    ram = 60.0 * ra / 15.0
    rah = int(np.floor(ram / 60.0))
    ram -= 60.0 * rah

    des = np.sign(de)
    dem = 60.0 * np.abs(de)
    ded = int(np.floor(dem / 60.0))
    dem -= 60.0 * ded

    if des == -1:
        sign = "-"
    else:
        sign = "+"

    return ("%02d%06.3f%c%02d%05.2f" % (rah, ram, sign, ded, dem)).replace(
        ".", "")
