# screenToGrid
#
# Copied verbatim from https://github.com/JnyJny/DungeonGenerator
#   file Dungeon.py, line 51
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Procedural and generated worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def roundm(n,m):
    rnd = lambda x: math.floor((x+m-1)/m)*m
    try:
        return [x for x in rnd(n)]
    except TypeError:
        return rnd(n)


def screenToGrid(coord,spacing):
    '''
    Convert screen coordinates to grid coordinates
    '''
    return roundm(coord/(spacing+1),spacing)
