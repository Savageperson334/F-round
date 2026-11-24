# pack_numbered_designation
#
# Copied verbatim from https://github.com/rlseaman/neolyzer
#   file src/designation_utils.py, line 30
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


def pack_numbered_designation(number):
    """
    Pack a numbered asteroid designation

    Examples:
    - 433 → 00433
    - 100004 → A0004
    - 360000 → a0000
    - 620000 → ~0000
    - 620061 → ~000z
    - 3140113 → ~AZaz

    Format: ~NNNNN where ~ can be 0-9 for numbers < 100000
    or A-Z, a-z for 100000-619999, or ~ + base-62 for >= 620000
    """
    number = int(number)

    if number < 0:
        raise ValueError("Negative asteroid numbers not allowed")

    if number < 100000:
        # Simple case: pad with leading zeros
        return f"{number:05d}"
    elif number < 620000:
        # Use first character as base-62 for 100000s place
        hundreds_thousands = number // 10000
        remainder = number % 10000
        return encode_base62(hundreds_thousands) + f"{remainder:04d}"
    else:
        # High numbers: ~XXXX where XXXX is base-62 encoded (number - 620000)
        value = number - 620000
        # Encode as 4-digit base-62
        encoded = ''
        for _ in range(4):
            encoded = encode_base62(value % 62) + encoded
            value //= 62
        return '~' + encoded
