# add_cube_faces
#
# Copied verbatim from https://github.com/ExcaliburZero/blendplot
#   file blendplot/obj_graph.py, line 43
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def add_cube_faces(cube_str, start_num):
    """
    Appends the described cube faces to the given string.

    Parameters
    ----------
    cube_str : str
        the curent string representation of the cube
    start_num : int
        the last used vertex number
    """
    face_permutations = [
                (1,2,3,4),
                (5,8,7,6),
                (1,5,6,2),
                (2,6,7,3),
                (3,7,8,4),
                (5,1,4,8)
            ]
    for perm in face_permutations:
        cube_str += "f %s %s %s %s\n" % (
                    start_num + perm[0],
                    start_num + perm[1],
                    start_num + perm[2],
                    start_num + perm[3]
                )
    return cube_str
