# encode_base62
#
# Copied verbatim from https://github.com/rlseaman/neolyzer
#   file src/designation_utils.py, line 17
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

PACK_CHARS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


def encode_base62(num):
    """Convert number to base-62 character (0-9, A-Z, a-z)"""
    if num < 0 or num >= 62:
        raise ValueError(f"Number {num} out of range for base-62 encoding")
    return PACK_CHARS[num]
