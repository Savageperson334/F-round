# mjd_to_cln
#
# Copied verbatim from https://github.com/rlseaman/neolyzer
#   file src/database.py, line 27
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np

CLN_EPOCH_JD = 2444240.0076

SYNODIC_MONTH = 29.530588853


def mjd_to_cln(mjd):
    """Convert MJD to Catalina Lunation Number (integer).

    Uses average synodic month - fast and consistent for filtering.
    """
    if mjd is None:
        return None
    jd = mjd + 2400000.5
    days_from_epoch = jd - CLN_EPOCH_JD
    lunations = days_from_epoch / SYNODIC_MONTH
    return int(np.floor(lunations))
