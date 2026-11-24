# money
#
# Copied verbatim from https://github.com/AkshayTallikar/software-archaeology
#   file modern_library/main.py, line 198
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def money(cents: int) -> str:
    """Format cents as a two-decimal string such as "0.75" or "10.00"."""
    return f"{cents // 100}.{cents % 100:02d}"
