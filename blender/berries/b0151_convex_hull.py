# convex_hull
#
# Copied verbatim from https://github.com/DarkGeekMS/artistic-style-transfer-using-texture-synthesis
#   file utils/segment.py, line 96
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Textures and materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def cross(o, a, b):
    """
        Calculate the cross product between oa ans ob vectors,
        Args:
            o: RGB image.
            a:
            b:

        Returns:
            the cross product magnitude, positive value if oab makes CCW turn , negative for CW turn, zero if points are collinear.
    """
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def convex_hull(points):
    """
        Computes the convex hull of a set of 2D points.

        Args:
            points: list of 2D array representing the points.
        Returns:
            a list of vertices of the convex hull in counter-clockwise order,
            starting from the vertex with the lexicographically smallest coordinates.
    """

    # Sort the points.
    points.sort(key = lambda points: points[1])

    # Boring case: no points or a single point, possibly repeated multiple times.
    if len(points) <= 1:
        return points

    # Build lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Concatenation of the lower and upper hulls gives the convex hull.
    # Last point of each list is omitted because it is repeated at the beginning of the other list.
    return lower[:-1] + upper[:-1]
