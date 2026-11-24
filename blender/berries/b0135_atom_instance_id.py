# atom_instance_id
#
# Copied verbatim from https://github.com/Christanding/CrystalSketch
#   file src/crystalsketch/structures/periodic_images.py, line 179
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Molecular shapes and crystal lattices
#   the same function also appears in: touchbr/Graphite
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

CANONICAL_IMAGE_OFFSET = (0, 0, 0)


def atom_instance_id(site_id: str, image_offset: tuple[int, int, int]) -> str:
    if image_offset == CANONICAL_IMAGE_OFFSET:
        return site_id
    return f"{site_id}-image-{image_offset[0]}-{image_offset[1]}-{image_offset[2]}"
