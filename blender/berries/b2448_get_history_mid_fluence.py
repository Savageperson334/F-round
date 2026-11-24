# get_history_mid_fluence
#
# Copied verbatim from https://github.com/jlanversin/ONIX
#   file onix/nax/functions.py, line 1080
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def get_history_mid_fluence(history_fluence, step_break_indexes):

    history_mid_fluence = []
    for i in range(len(history_fluence)-1):
        # if i in step_break_indexes:
        #   continue
        history_mid_fluence.append((history_fluence[i+1]+history_fluence[i])/2)

    return history_mid_fluence
