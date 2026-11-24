# typecode
#
# Copied verbatim from https://github.com/citiesskylines-csur/CSUR
#   file core/csur.py, line 33
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Procedural and generated worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def typecode(roadtype):
    if roadtype == 'b':
        return ""
    else:
        return roadtype.upper()
