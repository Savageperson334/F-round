# isempty
#
# Copied verbatim from https://github.com/citiesskylines-csur/CSUR
#   file prefab/xmlserializer.py, line 5
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Procedural and generated worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def isempty(data):
    if data is None:
        return True
    if type(data) == dict:
        for v in data.values():
            if v != None and v != []:
                return False
        return True
    else:
        return not bool(data)
