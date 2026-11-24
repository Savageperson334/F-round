# pack_designation
#
# Copied verbatim from https://github.com/rlseaman/neolyzer
#   file src/designation_utils.py, line 264
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re

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


def pack_provisional_designation(desig):
    """
    Pack a provisional designation

    Examples:
    - 1979 XB → J79X00B
    - 1998 SQ108 → J98SA8Q
    - 2024 AA → K24A00A
    - 2007 TA418 → K07Tf8A

    Format: CYYHC##L where:
    - C: century (I=18, J=19, K=20)
    - YY: year within century
    - H: half-month letter (A-Y, skipping I)
    - C: cycle letter (A-Z for cycles 1-26, or base-62 for higher)
    - ##: cycle number in base-62
    - L: second letter if designation has two letters (e.g., SQ)

    The format is actually CYYHMLLN where:
    - H is half-month
    - M is first letter of cycle indicator
    - LL is cycle number (can be encoded)
    - N is second half-month letter if present
    """
    # Parse provisional designation: YYYY XX### or YYYY X# or YYYY XX
    match = re.match(r'^(\d{4})\s+([A-Z])([A-Z]?)(\d*)$', desig.strip())
    if not match:
        raise ValueError(f"Invalid provisional designation format: {desig}")

    year_str, first_letter, second_letter, number_str = match.groups()
    year = int(year_str)

    # Century encoding
    if 1800 <= year < 1900:
        century = 'I'
    elif 1900 <= year < 2000:
        century = 'J'
    elif 2000 <= year < 2100:
        century = 'K'
    else:
        raise ValueError(f"Year {year} outside supported range (1800-2099)")

    # Year within century
    year_in_century = year % 100

    # Half-month letter
    half_month = first_letter

    # Cycle number
    cycle_num = int(number_str) if number_str else 0

    # Encode cycle number
    if cycle_num == 0:
        # No cycle
        cycle_enc = '00'
    elif cycle_num < 10:
        # Single digit - encode as 0# where # is the digit
        cycle_enc = f"0{cycle_num}"
    elif cycle_num < 100:
        # Two digits - encode directly
        cycle_enc = f"{cycle_num:02d}"
    else:
        # Larger number - use base-62 encoding
        # Cycle 100 = 10*10, so we encode tens and ones separately
        tens_digit = cycle_num // 10
        ones_digit = cycle_num % 10
        cycle_enc = encode_base62(tens_digit) + str(ones_digit)

    # Second letter (if present)
    second_char = second_letter if second_letter else ''

    # Build packed designation
    packed = f"{century}{year_in_century:02d}{half_month}{cycle_enc}{second_char}"

    return packed


def pack_designation(desig):
    """
    Pack any designation (numbered or provisional)

    Examples:
    - '433' → '00433'
    - '100004' → 'A0004'
    - '1979 XB' → 'J79X00B'
    - '2024 AA' → 'K24A00A'
    - '6344 P-L' → 'PLS6344' (Palomar-Leiden Survey special case)
    """
    desig = desig.strip().replace('(', '').replace(')', '')

    # Special case: Palomar-Leiden Survey format (e.g., "6344 P-L")
    if ' P-L' in desig:
        try:
            number = desig.split()[0]  # Extract number before space
            return f"PLS{number}"
        except:
            pass

    # Check if it's a numbered asteroid (all digits)
    if desig.isdigit():
        return pack_numbered_designation(int(desig))

    # Check if it's a provisional designation (YYYY XX...)
    if re.match(r'^\d{4}\s+[A-Z]', desig):
        return pack_provisional_designation(desig)

    # Already packed or unknown format
    return desig
