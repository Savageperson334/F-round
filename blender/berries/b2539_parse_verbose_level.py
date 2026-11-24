# parse_verbose_level
#
# Copied verbatim from https://github.com/la-niche/nonos
#   file cli/src/nonos_cli/logging.py, line 31
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def parse_verbose_level(verbose: int) -> str:
    levels = ["WARNING", "INFO", "DEBUG"]
    level = levels[min(len(levels) - 1, verbose)]  # capped to number of levels
    return level
