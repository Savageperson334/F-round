# difference_between_geographic_angles
#
# Copied verbatim from https://github.com/mtomasini/PytheasSimulator
#   file src/pytheas_simulator/utilities.py, line 103
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def difference_between_geographic_angles(bearing: float, angle_wind: float) -> float:
    """
    Calculate the difference between geographic angles. Used to turn the absolute wind angle into the wind angle with the respect to the boat.

    Args:
        bearing (float): Bearing of the boat (in degrees).
        angle_wind (float): Absolute angle of the wind (in degrees).

    Returns:
        float: Returns the angle of the wind with respect to the boat (in degrees).
    """
    # first, turn angle into the range -180, 180
    if bearing > 180:
        bearing -= 360
    if angle_wind > 180:
        angle_wind -= 360

    effective_wind_angle = angle_wind - bearing

    if effective_wind_angle > 180:
        effective_wind_angle = 360 - effective_wind_angle
    if effective_wind_angle < -180:
        effective_wind_angle = 360 + effective_wind_angle

    return effective_wind_angle
