# pair_key
#
# Copied verbatim from https://github.com/ymatterlab/ycrystal
#   file src/ycrystal/core/bonds.py, line 32
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Molecular shapes and crystal lattices
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

Pair = tuple[str, str]


def pair_key(a: str, b: str) -> Pair:
    """Return the two element symbols in alphabetical order for a pair key."""
    return (a, b) if a <= b else (b, a)
