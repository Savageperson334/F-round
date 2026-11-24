# clean_list
#
# Copied verbatim from https://github.com/donjpierce/traffic
#   file models.py, line 100
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Public transport and city motion
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def clean_list(alist):
    """
    Simply removes duplicates from a list

    :param   alist: list
    :return clean: list
    """
    clean = []
    for i in range(len(alist)):
        if (i < len(alist) - 1) and (alist[i] != alist[i + 1]):
            clean.append(alist[i])

    clean.append(alist[-1])
    return clean
