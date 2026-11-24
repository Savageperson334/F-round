# new_route_decompiler
#
# Copied verbatim from https://github.com/donjpierce/traffic
#   file models.py, line 140
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Public transport and city motion
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def new_route_decompiler(new_path):
    """
    Decompiles a new_path from nav.build_new_route

    :param      new_path:
    :return:  clean_path:
    """
    clean_path = []
    for i in range(len(new_path)):
        if (i < len(new_path) - 1) and (new_path[i] != new_path[i + 1]):
            clean_path.append(new_path[i])
    clean_path.append(new_path[-1])
    return clean_path
