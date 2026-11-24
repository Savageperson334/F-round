# error_flag
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/util/util.py, line 235
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def error_flag(pred, actual, dev=1.0, method=1):
    """
    Calculate the difference between a predicted and an actual curve
    and return a log flagging large differences based on a user-defined
    distance (in standard deviation units) from the mean difference.

    Author:
        Matteo Niccoli, 2018

    Args:
        predicted (ndarray): predicted log.
        actual (ndarray):  original log.
        dev (float): standard deviations to use, default 1
        error calcluation method (int): default 1
            1: difference between curves larger than mean difference plus dev
            2: curve slopes have opposite sign. Will require depth log for .diff method
            3: curve slopes of opposite sign OR difference larger than mean plus dev
    Returns:
        flag (ndarray) =  error flag curve
    """
    flag = np.zeros(len(pred))
    err = np.abs(pred-actual)
    err_mean = np.mean(err)
    err_std = np.std(err)

    if method == 1:
        flag[np.where(err > (err_mean + (dev * err_std)))] = 1

    return flag
