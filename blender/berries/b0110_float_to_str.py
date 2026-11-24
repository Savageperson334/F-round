# float_to_str
#
# Copied verbatim from https://github.com/BiologyHazard/music-box-designer
#   file music_box_designer/fmp/fmp_v1.py, line 115
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Mechanical music boxes and organs
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def float_to_str(x: float) -> str:
    if x == round(x):
        return str(round(x))
    return str(x)
