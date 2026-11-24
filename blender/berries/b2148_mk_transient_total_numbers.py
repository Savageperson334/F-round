# mk_transient_total_numbers
#
# Copied verbatim from https://github.com/gvard/astrodata
#   file src/astrodata/stars/transients.py, line 115
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def mk_transient_total_numbers(total_dct):
    """Make list of transient total numbers."""
    total_lst = []
    _sum = 0
    for num in total_dct.values():
        if _sum == 0:
            _sum = num
        else:
            _sum += num
        total_lst.append(_sum)
    return total_lst
