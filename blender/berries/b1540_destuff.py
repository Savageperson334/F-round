# destuff
#
# Copied verbatim from https://github.com/daniestevez/gr-satellites
#   file python/eseo_line_decoder.py, line 20
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sensors and telemetry
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def destuff(x):
    y = list()
    run = 0
    for i, bit in enumerate(x):
        if run == 5:
            if bit == 1:
                # Unexpected long run of ones
                return
            else:
                run = 0
        elif bit == 0:
            run = 0
            y.append(bit)
        elif bit == 1:
            run += 1
            y.append(bit)
    return np.array(y, dtype='uint8')
