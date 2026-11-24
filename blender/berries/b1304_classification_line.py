# classification_line
#
# Copied verbatim from https://github.com/c64cryptoboy/retro-archaeology-skills
#   file skills/retrodebugger-windows-build/scripts/analyze_build_log.py, line 66
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re

ECHO_COMMAND = re.compile(r"^\s*(?:\+\s*)?(?:echo|Write-Host|Write-Output)(?=\s|$)", re.IGNORECASE)

PROJECT_PREFIX = re.compile(r"^\s*\d+>\s*")


def classification_line(line: str) -> str | None:
    normalized = PROJECT_PREFIX.sub("", line, count=1)
    return None if ECHO_COMMAND.match(normalized) else normalized
