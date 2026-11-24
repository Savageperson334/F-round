# quantize_float
#
# Copied verbatim from https://github.com/farjon/insect_detection
#   file pytorch_image_models/timm/models/regnet.py, line 102
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Moths insects and insect traps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def quantize_float(f, q):
    """Converts a float to closest non-zero int divisible by q."""
    return int(round(f / q) * q)
