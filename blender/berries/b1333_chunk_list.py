# chunk_list
#
# Copied verbatim from https://github.com/cbassa/stvid
#   file process.py, line 51
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def chunk_list(l, n):
    o = []
    for i in range(0, len(l), n):
        o.append(l[i:i + n])
    return o
