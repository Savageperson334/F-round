# f32
#
# Copied verbatim from https://github.com/Worldwave/Wakes
#   file tools/gen_scales.py, line 51
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import struct


def f32(x):
    """x rounded to a C float."""
    return struct.unpack('<f', struct.pack('<f', x))[0]
