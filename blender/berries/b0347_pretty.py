# pretty
#
# Copied verbatim from https://github.com/JeremyPorquez/CRASHyperspectralAnalysis
#   file HSA/pyqtgraph/debug.py, line 1092
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Microscopy & small worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def pretty(data, indent=''):
    """Format nested dict/list/tuple structures into a more human-readable string
    This function is a bit better than pprint for displaying OrderedDicts.
    """
    ret = ""
    ind2 = indent + "    "
    if isinstance(data, dict):
        ret = indent+"{\n"
        for k, v in data.iteritems():
            ret += ind2 + repr(k) + ":  " + pretty(v, ind2).strip() + "\n"
        ret += indent+"}\n"
    elif isinstance(data, list) or isinstance(data, tuple):
        s = repr(data)
        if len(s) < 40:
            ret += indent + s
        else:
            if isinstance(data, list):
                d = '[]'
            else:
                d = '()'
            ret = indent+d[0]+"\n"
            for i, v in enumerate(data):
                ret += ind2 + str(i) + ":  " + pretty(v, ind2).strip() + "\n"
            ret += indent+d[1]+"\n"
    else:
        ret += indent + repr(data)
    return ret
