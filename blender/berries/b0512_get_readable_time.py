# get_readable_time
#
# Copied verbatim from https://github.com/MartinThoma/hwrt
#   file hwrt/utils.py, line 336
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def get_readable_time(duration: int) -> str:
    """
    Format the time to a readable format.

    Parameters
    ----------
    duration : int
        Time in ms

    Returns
    -------
    string
        The time splitted to highest used time (minutes, hours, ...)
    """
    ms = duration % 1000
    duration -= ms
    duration //= 1000

    sec = duration % 60
    duration -= sec
    duration //= 60

    minutes = duration % 60
    duration -= minutes
    duration //= 60

    if duration != 0:
        return "%ih, %i minutes %is %ims" % (duration, minutes, sec, ms)
    elif minutes != 0:
        return "%i minutes %is %ims" % (minutes, sec, ms)
    elif sec != 0:
        return "%is %ims" % (sec, ms)
    else:
        return "%ims" % ms
