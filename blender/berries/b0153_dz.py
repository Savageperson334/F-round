# dz
#
# Copied verbatim from https://github.com/Dean-Zylman/RoArm-Ps4-Controller
#   file ps4_robot_arm_control.py, line 112
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Robots and tactile mechanisms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def dz(v, deadzone=0.12):
    """
    Deadzone filter to remove joystick noise.
    """
    return 0 if abs(v) < deadzone else v
