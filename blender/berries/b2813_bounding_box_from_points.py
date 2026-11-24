# bounding_box_from_points
#
# Copied verbatim from https://github.com/mtomasini/PytheasSimulator
#   file src/pytheas_simulator/utilities.py, line 252
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def bounding_box_from_points(departure_coordinates, arrival_coordinates, buffer = 1):
    """Calculates a geographic bounding box given two locations. 

    Args:
        departure_coordinates (Tuple[float, float]): departure site in format [latitude, longitude]
        arrival_coordinates (Tuple[float, float]): arrival site in format [latitude, longitude]
        buffer (float): size of the bounding box margins (in degrees).

    Returns:
        Tuple[float, float, float, float]: the bounding box in format [minimal lat, min lon, max lat, max lon]
    """
    departure_lat = departure_coordinates[0]
    departure_lon = departure_coordinates[1]
    arrival_lat = arrival_coordinates[0]
    arrival_lon = arrival_coordinates[1]

    min_lat = min(departure_lat, arrival_lat) - buffer
    max_lat = max(departure_lat, arrival_lat) + buffer
    min_lon = min(departure_lon, arrival_lon) - buffer
    max_lon = max(departure_lon, arrival_lon) + buffer

    return [min_lat, min_lon, max_lat, max_lon]
