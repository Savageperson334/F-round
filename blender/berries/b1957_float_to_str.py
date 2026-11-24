# float_to_str
#
# Copied verbatim from https://github.com/giojacuzzi/few-shot-transfer-learning-bioacoustics
#   file src/gui.py, line 108
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Animal acoustics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def float_to_str(value: float, step_size: float):
    value = float(value)
    digits = len(str(step_size).split('.')[-1])
    return(f"{round(value, digits):.{digits}f}")
