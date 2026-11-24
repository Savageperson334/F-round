# normalize_element_symbol
#
# Copied verbatim from https://github.com/Christanding/CrystalSketch
#   file src/crystalsketch/structures/periodic_images.py, line 215
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Molecular shapes and crystal lattices
#   the same function also appears in: touchbr/Graphite
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def normalize_element_symbol(symbol: str) -> str:
    normalized = symbol.strip()
    if not normalized:
        raise ValueError("Element symbol cannot be empty.")
    return normalized[0].upper() + normalized[1:].lower()
