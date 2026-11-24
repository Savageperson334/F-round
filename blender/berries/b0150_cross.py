# cross
#
# Copied verbatim from https://github.com/DarkGeekMS/artistic-style-transfer-using-texture-synthesis
#   file utils/segment.py, line 83
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
