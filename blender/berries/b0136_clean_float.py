# clean_float
#
# Copied verbatim from https://github.com/Christanding/CrystalSketch
#   file src/crystalsketch/structures/periodic_images.py, line 202
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Molecular shapes and crystal lattices
#   the same function also appears in: touchbr/Graphite
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math

FLOAT_ZERO_TOLERANCE = 1e-12


def clean_float(value: float) -> float:
    cleaned = float(value)
    if math.isclose(cleaned, 0.0, abs_tol=FLOAT_ZERO_TOLERANCE):
        return 0.0
    return cleaned
