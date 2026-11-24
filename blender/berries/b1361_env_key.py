# env_key
#
# Copied verbatim from https://github.com/chrisfulcher/orrery
#   file src/orrery/config.py, line 118
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def env_key(field: str) -> str:
    """``sam_api_key`` -> ``ORRERY_SAM_API_KEY``."""
    return "ORRERY_" + field.upper()
