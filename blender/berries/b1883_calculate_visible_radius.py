# calculate_visible_radius
#
# Copied verbatim from https://github.com/fisadev/sateye
#   file website/static/website/py/sateye_client/utils.py, line 54
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math

EARTH_CIRCUNFERENCE = 40075000

EARTH_RADIUS = 6371000


def calculate_visible_radius(altitude):
    """
    Calculate the radius of the visible area for a satellite at a given altitude.
    """
    # angle between a line going from the center of the Earth to the satellite, and another
    # line going from the center of the earth to the horizon line of the satellite
    visible_angle = math.degrees(
        math.acos(EARTH_RADIUS / (EARTH_RADIUS + altitude))
    )
    # distance over the surface of the earth, from the satellite coordinates, to its
    # horizon
    return (visible_angle / 360) * EARTH_CIRCUNFERENCE
