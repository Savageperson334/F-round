# isleft
#
# Copied verbatim from https://github.com/anshdavid/Procedural-City-Generation
#   file procedural_city_generation/building_generation/roofs.py, line 133
#   licence (as GitHub reports it): MPL-2.0   see ../licenses/
#   catalogue shelf: Procedural and generated worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def isleft(wall, point):
    """Helper function for p_in_poly
    Taken from: http://geomalgorithms.com/a03-_inclusion.html, all credits to Dan Sunday.


    Paramaters
    ----------
    wall : numpy-array with shape 3, 2
    point : numpy-array with shape 3, 1

    Returns
    -------
    float
    """
    return ((wall[1][0]-wall[0][0])*(point[1]-wall[0][1]) - (point[0]-wall[0][0]) * (wall[1][1]-wall[0][1]))
