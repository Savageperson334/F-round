# f32
#
# Copied verbatim from https://github.com/jbschooley/Virtual-FM-1
#   file engines/choralroot/upstream/tools/gen_tables.py, line 28
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import struct


def f32(x):
    """x rounded to an IEEE single, as C stores a float"""
    return struct.unpack("f", struct.pack("f", x))[0]
