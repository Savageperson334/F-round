# ms
#
# Copied verbatim from https://github.com/Technoculture/openoligo-firmware
#   file openoligo/utils/wait.py, line 25
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def ms(seconds: float) -> float:  # pylint: disable=invalid-name
    """Convert seconds to milliseconds."""
    return seconds / 1000
