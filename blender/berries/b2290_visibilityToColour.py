# visibilityToColour
#
# Copied verbatim from https://github.com/iotdesignshop/mediapipe-robot-arm-controller
#   file controller.py, line 17
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Robots and tactile mechanisms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def visibilityToColour(vis):
  if (vis < 0.5):
    return (0, 0, 255)  # Red - low visibility
  elif (vis < 0.75):
    return (0,255,255)  # Yellow - medium visibility
  else:
    return (0, 255, 0)
