# list2string
#
# Copied verbatim from https://github.com/hvasbath/beat
#   file beat/utility.py, line 1181
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def slice2string(slice_obj):
    """
    Wrapper for better formatted string method for slices.

    Returns
    -------
    str
    """
    if isinstance(slice_obj, slice):
        if slice_obj.step:
            return "{}:{}:{}".format(slice_obj.start, slice_obj.stop, slice_obj.step)
        else:
            return "{}:{}".format(slice_obj.start, slice_obj.stop)
    else:
        return slice_obj


def list2string(any_list, fill=", "):
    """
    Convert list of string to single string.

    Parameters
    ----------
    l: list
        of strings
    """
    return fill.join("%s" % slice2string(listentry) for listentry in any_list)
