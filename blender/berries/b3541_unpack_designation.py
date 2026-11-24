# unpack_designation
#
# Copied verbatim from https://github.com/rlseaman/neolyzer
#   file scripts/diagnostics/diagnose_sbdb.py, line 69
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def unpack_designation(packed):
    """Convert packed MPC designation to unpacked format"""
    if not packed:
        return packed

    # Numbered asteroids (all digits or leading spaces + digits)
    packed = packed.strip()
    if packed.isdigit():
        return packed.lstrip('0') or '0'

    # Check for packed number format (A0000, B0000, etc.)
    if len(packed) >= 5 and packed[0].isalpha() and packed[1:].isdigit():
        first_char = packed[0]
        number_part = int(packed[1:])

        char_values = {
            'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
            'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21,
            'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27,
            'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33,
            'Y': 34, 'Z': 35, 'a': 36, 'b': 37, 'c': 38, 'd': 39,
            'e': 40, 'f': 41, 'g': 42, 'h': 43, 'i': 44, 'j': 45,
            'k': 46, 'l': 47, 'm': 48, 'n': 49, 'o': 50, 'p': 51,
            'q': 52, 'r': 53, 's': 54, 't': 55, 'u': 56, 'v': 57,
            'w': 58, 'x': 59, 'y': 60, 'z': 61
        }

        if first_char in char_values:
            full_number = char_values[first_char] * 10000 + number_part
            return str(full_number)

    # Provisional designations (e.g., K24A00A -> 2024 AA)
    if len(packed) == 7:
        century_codes = {'I': '18', 'J': '19', 'K': '20', 'L': '21'}
        half_month_codes = 'ABCDEFGHJKLMNOPQRSTUVWXY'
        second_letter_codes = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

        century_char = packed[0]
        year_digits = packed[1:3]
        half_month = packed[3]
        cycle_code = packed[4:6]
        second_letter = packed[6]

        if century_char in century_codes and half_month in half_month_codes:
            year = century_codes[century_char] + year_digits

            # Decode cycle number
            if cycle_code == '00':
                cycle_num = 0
            else:
                cycle_num = 0
                if cycle_code[0] in second_letter_codes:
                    cycle_num += second_letter_codes.index(cycle_code[0]) * 62
                if cycle_code[1] in second_letter_codes:
                    cycle_num += second_letter_codes.index(cycle_code[1])

            if cycle_num == 0:
                return f"{year} {half_month}{second_letter}"
            else:
                return f"{year} {half_month}{second_letter}{cycle_num}"

    # If we can't unpack, return as-is
    return packed
