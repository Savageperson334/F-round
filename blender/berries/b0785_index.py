# index
#
# Copied verbatim from https://github.com/aaronjolson/Blender-Python-Procedural-Level-Generation
#   file Blender_2_7/recursive_backtracking_maze.py, line 158
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Procedural and generated worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

cols = 10

rows = 10


def index(x, y):
    if x < 0 or y < 0 or x > cols - 1 or y > rows - 1:
        return None
    else:
        return x + y * cols
