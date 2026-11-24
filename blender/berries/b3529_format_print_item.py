# format_print_item
#
# Copied verbatim from https://github.com/ringger/basicoco
#   file emulator/ast_nodes.py, line 54
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Retro computing
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

SIGNIFICANT_DIGITS = 9


def format_basic_number(value) -> str:
    """Digits of a number as Color BASIC prints them, without the leading
    sign-position space: 3, -2.5, .333333333, -.5, 1.26765061E+30, 1E-03.

    Up to 9 significant digits, no leading zero before the decimal point,
    trailing zeros dropped. Magnitudes from .01 up to 999,999,999 print in
    fixed notation; anything else in E notation.
    """
    if isinstance(value, bool):
        value = -1 if value else 0
    if isinstance(value, int) and abs(value) < 10 ** SIGNIFICANT_DIGITS:
        return str(value)
    value = float(value)
    if value == 0:
        return '0'
    magnitude = abs(value)
    rounded = float(f'{magnitude:.{SIGNIFICANT_DIGITS}g}')
    sign = '-' if value < 0 else ''
    if 0.01 <= rounded < 10 ** SIGNIFICANT_DIGITS:
        digits = f'{rounded:.{SIGNIFICANT_DIGITS}f}'.rstrip('0').rstrip('.')
        if digits.startswith('0.'):
            digits = digits[1:]
        return sign + digits
    mantissa, exponent = f'{rounded:.{SIGNIFICANT_DIGITS - 1}e}'.split('e')
    mantissa = mantissa.rstrip('0').rstrip('.')
    exp_value = int(exponent)
    return f"{sign}{mantissa}E{'+' if exp_value >= 0 else '-'}{abs(exp_value):02d}"


def format_print_item(value) -> str:
    """A value as PRINT and PRINT# write it: strings as they are; numbers
    with a sign position (space or '-') in front and a space after,
    so ' 5 ', '-3 ', ' .5 '."""
    if isinstance(value, str):
        return value
    if isinstance(value, (int, float)):
        digits = format_basic_number(value)
        return digits + ' ' if value < 0 else ' ' + digits + ' '
    return str(value)
