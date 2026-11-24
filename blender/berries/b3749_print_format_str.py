# print_format_str
#
# Copied verbatim from https://github.com/timpol/DQPB
#   file dqpb/util.py, line 136
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def print_format_str(d_places, sci=False):
    """
    """
    d_places = int(d_places)

    if not sci:
        bs = "#,##0"
        if d_places > 0:
            fs = bs + '.' + d_places * '0'
        else:
            fs = bs
    else:
        bs1 = "0.0"
        bs2 = "E+00"
        if d_places > 0:
            fs = bs1 + (d_places - 1) * "0" + bs2
        else:
            fs = bs1 + bs2

    return fs
