# reynolds_pipe
#
# Copied verbatim from https://github.com/patrickscottbest/balloonwars
#   file balloonwars.py, line 13
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Weather balloon telemetry
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def reynolds_pipe(density, velocity, diameter, viscosity):
    """
    Calculate the Reynolds number for a given pipe flow.
    The resulting Reynolds number is dimensionless. 
    It is used to characterize flow patterns.

    Arguments:
    density -- density of the fluid in [kg/m3]
    velocity -- the mean velocity of the fluid in [m/s]
    viscosity -- dynamic viscosity of the fluid in [Pa*s]
    diameter -- inside diameter of the pipe in [m]
    """
    return density * velocity * diameter / viscosity
