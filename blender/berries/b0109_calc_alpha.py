# calc_alpha
#
# Copied verbatim from https://github.com/BiologyHazard/music-box-designer
#   file music_box_designer/draft.py, line 1629
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Mechanical music boxes and organs
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def calc_alpha(radius: float, distance: float) -> float:
    if distance <= radius - 1 / 2:
        return 1
    if distance >= radius + 1 / 2:
        return 0
    return radius + 1 / 2 - distance
