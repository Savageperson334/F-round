# scale_point_in_rect
#
# Copied verbatim from https://github.com/holmos-ipm/holmos-rpi
#   file other/pc_client/holmos_pc_main.py, line 105
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Optical computing and holograms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def scale_point_in_rect(xy_from, wh_from, wh_to):
    """
    scale a 2D point from one rectangle to another
    :param xy_from: point in "from" rectangle
    :param wh_from: size of "from" rectangle
    :param wh_to: size of "to" rectangle
    :return: (x_to, y_to) float(!) coordinates in "to" rectangle
    """
    return tuple(coord_from / size_from * size_to for coord_from, size_from, size_to in zip(xy_from, wh_from, wh_to))
