# add_image_offsets
#
# Copied verbatim from https://github.com/Christanding/CrystalSketch
#   file src/crystalsketch/structures/periodic_images.py, line 291
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Molecular shapes and crystal lattices
#   the same function also appears in: touchbr/Graphite
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def add_image_offsets(
    left: tuple[int, int, int],
    right: tuple[int, int, int],
) -> tuple[int, int, int]:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])
