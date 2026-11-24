# get_changes
#
# Copied verbatim from https://github.com/amidos2006/gym-pcgrl
#   file gym_pcgrl/envs/helper.py, line 120
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Procedural and generated worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def get_changes(map, vertical=False):
    start_y = 0
    start_x = 0
    if vertical:
        start_y = 1
    else:
        start_x = 1
    value = 0
    for y in range(start_y, len(map)):
        for x in range(start_x, len(map[y])):
            same = False
            if vertical:
                same = map[y][x] == map[y-1][x]
            else:
                same = map[y][x] == map[y][x-1]
            if not same:
                value += 1
    return value
