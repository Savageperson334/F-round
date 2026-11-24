# mm_from_pixels
#
# Copied verbatim from https://github.com/ymatterlab/ycrystal
#   file src/ycrystal/core/export.py, line 133
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Molecular shapes and crystal lattices
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

MM_PER_INCH = 25.4


def mm_from_pixels(pixels: float, dpi: float) -> float:
    """Return the physical length of ``pixels`` at ``dpi``, in millimetres."""
    return float(pixels) / float(dpi) * MM_PER_INCH
