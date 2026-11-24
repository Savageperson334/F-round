# slope
#
# Copied verbatim from https://github.com/JnyJny/DungeonGenerator
#   file Dungeon.py, line 19
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Procedural and generated worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def slope(p0,p1):
    try:
        m = (p1[1] - p0[1]) / (p1[0] - p0[0])
    except ZeroDivisionError:        
        m = 0
    return m
