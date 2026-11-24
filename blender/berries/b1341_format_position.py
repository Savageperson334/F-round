# format_position
#
# Copied verbatim from https://github.com/cbassa/stvid
#   file stvid/fourframe.py, line 979
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def format_position(ra, de):
    # Right ascension
    rah = ra / 15
    ram = np.mod(60 * rah, 60)
    ram = np.round(ram * 1000) / 1000
    ram = np.mod(ram, 60)
    rah = np.round(rah - ram / 60)
    rah = np.mod(rah, 24)

    # Declination
    des = np.sign(de)
    dea = np.abs(de)
    dem = np.mod(60 * dea, 60)
    dem = np.round(dem * 100) / 100
    dem = np.mod(dem, 60)
    ded = np.round(dea - dem / 60)

    if des == -1:
        sign = "-"
    else:
        sign = "+"

    return ("%02d%06.3f%c%02d%05.2f" % (rah, ram, sign, ded, dem)).replace(".", "")
