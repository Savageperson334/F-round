# path_decompiler
#
# Copied verbatim from https://github.com/donjpierce/traffic
#   file models.py, line 116
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Public transport and city motion
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def path_decompiler(lines):
    """
    Decompiles a path from its geometry configuration into a pure list of tuples

    :param  lines:      list in geometric form according to osmnx 'geometry' feature
    :return new_path:   list of tuples
    """
    path = []
    for line in lines:
        for point in line:
            path.append(point)

    # the path must be cleaned of twin nodes for car dynamics
    # these are nodes which overlap (two nodes laying on top of each other on the same point)
    # OpenStreetMap has this issue
    clean_path = [] if len(path) else path
    if len(path):
        for i in range(len(path)):
            if (i < len(path) - 1) and (path[i] != path[i + 1]):
                clean_path.append(path[i])
        clean_path.append(path[-1])
    return clean_path
