# list_repeat
#
# Copied verbatim from https://github.com/hvasbath/beat
#   file beat/heart.py, line 610
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def list_repeat(arr, repeat=1):
    if isinstance(repeat, list):
        if len(repeat) != arr.size:
            raise ValueError(
                "Inconsistent requested dimensions! "
                "repeat: {}, {} array size".format(repeat, arr.size)
            )
        else:
            out_values = []
            for i, re in enumerate(repeat):
                out_values.append(num.repeat(arr[i], re))

            return num.hstack(out_values)
    else:
        return num.tile(arr, repeat)
