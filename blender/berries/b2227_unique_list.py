# unique_list
#
# Copied verbatim from https://github.com/hvasbath/beat
#   file beat/utility.py, line 1206
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def unique_list(any_list):
    """
    Find unique entries in list and return them in a list.
    Keeps variable order.

    Parameters
    ----------
    l : list

    Returns
    -------
    list with only unique elements
    """
    used = []
    return [x for x in any_list if x not in used and (used.append(x) or True)]
