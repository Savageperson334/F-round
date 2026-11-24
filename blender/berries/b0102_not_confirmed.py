# not_confirmed
#
# Copied verbatim from https://github.com/BAHALLA/orrery
#   file core/orrery_core/studio/compiler.py, line 290
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def not_confirmed(reason: str) -> dict[str, str]:
    """What the model gets for an action that was not sent (a neutral ``BLOCKED``)."""
    return {
        "status": "BLOCKED",
        "error": f"{reason} Do not retry it; say what you would have done.",
    }
