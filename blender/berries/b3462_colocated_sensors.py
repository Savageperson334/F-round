# colocated_sensors
#
# Copied verbatim from https://github.com/pyrocko/qseek
#   file src/qseek/station_weights.py, line 64
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np

COLOCATED_DISTANCE = 50.0


def colocated_sensors(distances: np.ndarray) -> np.ndarray:
    """Count the sensors of each station's site.

    Args:
        distances: Array of shape (n_stations, n_stations) with interstation
            distances in meters, NaN on the diagonal.

    Returns:
        Array of shape (n_stations,) with the number of sensors within
            `COLOCATED_DISTANCE`, including the station itself.
    """
    return 1 + np.sum(distances <= COLOCATED_DISTANCE, axis=1)
