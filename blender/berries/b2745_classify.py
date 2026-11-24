# classify
#
# Copied verbatim from https://github.com/microsoft/haste
#   file docker/training/code/output2visualizer.py, line 56
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def classify(x: float) -> int:
    thresholds = [0.2, 0.4, 0.6, 0.8]
    for i, threshold in enumerate(thresholds):
        if x <= threshold:
            return i
    return len(thresholds)
