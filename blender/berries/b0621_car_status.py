# car_status
#
# Copied verbatim from https://github.com/Pandas-Team/Autonomous-Car-Simulation-Based-on-AVIS-Engine-FIRA-2021
#   file RACE/functions.py, line 170
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Public transport and city motion
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def car_status(actual_where, sensors):
    rounded_where = int(np.round(actual_where))
    if rounded_where == 3:
        if (sensors[1] == 1500) and (sensors[2] == 1500) :
            print("clear")
            return 1

        elif sensors[1] != 1500 or (sensors[2] != 1500):
            print('obstacle on right, turn left')
            return 2


    elif rounded_where == 2:
        if (sensors[0] == 1500) and (sensors[1] == 1500) :
            print('Clear, go back to right')

            return 3
        elif (sensors[1] != 1500):
            print('Obstacle Ahead')

            return 4


    elif rounded_where == 1:
        pass

    elif rounded_where == 4:
        pass

    else:
         return 3
