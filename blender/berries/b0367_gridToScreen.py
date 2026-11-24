# gridToScreen
#
# Copied verbatim from https://github.com/JnyJny/DungeonGenerator
#   file Dungeon.py, line 45
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Procedural and generated worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def gridToScreen(count,spacing):
    '''
    Convert grid coordinates (counts) to screen coordinates
    '''
    return ((spacing+1)*count)+1
