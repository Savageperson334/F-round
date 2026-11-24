# convert2interleaved
#
# Copied verbatim from https://github.com/uba/tathu
#   file tathu/geometry/utils.py, line 13
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def convert2interleaved(e):
    '''
    Auxiliary function that converts an extent to interleaved format
    i.e. [llx, urx, lly, ury] --> [llx, lly, urx, ury]
    '''
    return (e[0], e[2], e[1], e[3])
