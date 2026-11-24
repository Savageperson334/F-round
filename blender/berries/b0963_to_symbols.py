# to_symbols
#
# Copied verbatim from https://github.com/alepersichetti/WyrmHex
#   file wyrmhex.py, line 1148
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Cave surveys and subterranean maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

SEED_SYMBOLS = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"


def to_symbols(value, length):
    """value written in base 32 with SEED_SYMBOLS, padded to length symbols."""
    symbols = ""
    for _ in range(length):
        value, digit = divmod(value, 32)
        symbols = SEED_SYMBOLS[digit] + symbols
    return symbols
