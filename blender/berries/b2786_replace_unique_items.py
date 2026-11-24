# replace_unique_items
#
# Copied verbatim from https://github.com/mnky9800n/Python-course-materials-for-seismology-students
#   file utilities/util.py, line 1
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def replace_unique_items(iterable, replace_with=None):
    """
    replaces items after the first unique item in a list
    with replace_with.

    ::default behavior::
    ----------------------------------
    In  : x = [1, 1, 2, 2]
    Out : replace_unique_items(x)
    [1, None, 2, None]
    """
    result = []
    for item in iterable:
        if item not in result:
            result.append(item)
        else:
            result.append(replace_with)
    return result
