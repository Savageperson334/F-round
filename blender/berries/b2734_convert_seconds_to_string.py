# convert_seconds_to_string
#
# Copied verbatim from https://github.com/mesoSPIM/mesoSPIM-control
#   file mesoSPIM/src/utils/utility_functions.py, line 50
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Microscopy & small worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def convert_seconds_to_string(delta_t):
    '''
    Converts an input value in seconds into a string in the format hh:mm:ss

    Interestingly, a variant using np.divmod is around 4-5x slower in initial tests.
    '''
    if delta_t <= 0:
        return '--:--:--'
    else:
        hours, remainder = divmod(delta_t, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
