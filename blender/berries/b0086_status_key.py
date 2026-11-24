# status_key
#
# Copied verbatim from https://github.com/BAHALLA/orrery
#   file agents/orrery-assistant/orrery_assistant/agent.py, line 171
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def status_key(key: str) -> str:
    """The state key a system's batch checker writes its report to."""
    return f"{key}_status"
