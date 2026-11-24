# fee_cents_for
#
# Copied verbatim from https://github.com/AkshayTallikar/software-archaeology
#   file modern_library/main.py, line 190
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

FEE_CAP_CENTS = 1000

FEE_FIRST_CHARGE_CENTS = 75

FEE_FREE_DAYS = 2

FEE_STEP_CENTS = 25


def fee_cents_for(days_late: int) -> int:
    """Late fee in cents for a given number of days late (see FEE_* above)."""
    if days_late <= FEE_FREE_DAYS:
        return 0
    charge = FEE_FIRST_CHARGE_CENTS + FEE_STEP_CENTS * (days_late - FEE_FREE_DAYS - 1)
    return min(charge, FEE_CAP_CENTS)
