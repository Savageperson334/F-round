# get_floor_dist
#
# Copied verbatim from https://github.com/amidos2006/gym-pcgrl
#   file gym_pcgrl/envs/helper.py, line 56
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Procedural and generated worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def _calc_dist_floor(map, x, y, types):
    for dy in range(len(map)):
        if y+dy >= len(map):
            break
        if map[y+dy][x] in types:
            return dy-1
    return len(map) - 1


def get_floor_dist(map, fromTypes, floorTypes):
    result = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] in fromTypes:
                result += _calc_dist_floor(map, x, y, floorTypes)
    return result
