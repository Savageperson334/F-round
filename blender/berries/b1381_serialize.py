# serialize
#
# Copied verbatim from https://github.com/citiesskylines-csur/CSUR
#   file prefab/xmlserializer.py, line 16
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Procedural and generated worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

TABSPACE = 2


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


def serialize(data, object_name, tablevel=0):
    indent = " " * tablevel * TABSPACE
    if isempty(data):
        return indent + "<%s />\n" % object_name
    if type(data) == list:
        string = ""
        for item in data:
            string += serialize(item, object_name, tablevel=tablevel+1)
        string += indent
    else:
        string = indent + "<%s>" % object_name
        if type(data) == dict:
            string += "\n"
            for k, v in data.items():
                string += serialize(v, k, tablevel=tablevel+1)
            string += indent
        else:
            string += str(data)
        string += "</%s>\n" % object_name
    return string
