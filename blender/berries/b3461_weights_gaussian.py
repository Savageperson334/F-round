# weights_gaussian
#
# Copied verbatim from https://github.com/pyrocko/qseek
#   file src/qseek/station_weights.py, line 32
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def weights_gaussian(
    distances: np.ndarray,
    distance_taper: float,
    required_stations: int = 4,
) -> np.ndarray:
    """Gaussian distance weights with a plateau of the closest stations.

    Args:
        distances: Array of shape (n_nodes, n_stations) with node-station distances
            in meters.
        distance_taper: Full width at half maximum of the Gaussian taper in meters.
        required_stations: Number of closest stations with full weight.

    Returns:
        Array of shape (n_nodes, n_stations) with weights between 0 and 1.
    """
    if required_stations < 1:
        raise ValueError("required_stations must be at least 1")

    required_stations = min(required_stations, distances.shape[1])
    sorted_distances = np.sort(distances, axis=1)
    threshold_distance = sorted_distances[:, required_stations - 1, np.newaxis]

    # Full width at half maximum (FWHM) to standard deviation conversion:
    # FWHM = 2.355 * sigma
    weights = np.exp(
        -(((distances - threshold_distance) ** 2) / (2 * (distance_taper / 2.355) ** 2))
    )
    weights[distances <= threshold_distance] = 1.0
    return weights
