# user_key
#
# Copied verbatim from https://github.com/BAHALLA/orrery
#   file core/orrery_core/plugins/token_budget_plugin.py, line 86
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import hashlib


def user_key(user_id: str) -> str:
    """The ledger key for *user_id*: bounded, printable, and not the subject itself."""
    return "user:" + hashlib.sha256(user_id.encode()).hexdigest()[:32]
