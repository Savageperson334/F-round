# apply_discount
#
# Copied verbatim from https://github.com/AkshayTallikar/software-archaeology
#   file modern_app/main.py, line 105
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from decimal import Decimal


def apply_discount(amount: Decimal, pct: int) -> Decimal:
    """Multiply by (100 - pct)%, exactly, with no rounding.

    Intermediate values are NOT truncated: rounding happens only at the two
    stage boundaries described in ``price_line`` and ``handle_invoice``.
    """
    return amount * (100 - pct) / 100
