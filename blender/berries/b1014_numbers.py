# numbers
#
# Copied verbatim from https://github.com/alexbarakov/amsterdam-by-building
#   file pipeline/s10_commons.py, line 74
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Historic cartography
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def numbers(spec):
    """'272' → [272]; '272tm284' or '272-284' → the even or odd numbers between; '281 283' → both."""
    m = re.match(r"(\d+)\s*(?:tm|t/m|-|–)\s*(\d+)$", spec)
    if m:
        a, b = int(m.group(1)), int(m.group(2))
        if 0 < b - a <= 24:
            return list(range(a, b + 1, 2))
    return [int(n) for n in re.findall(r"\d+", spec)][:4]
