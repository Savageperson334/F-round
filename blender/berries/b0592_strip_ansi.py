# strip_ansi
#
# Copied verbatim from https://github.com/NDilanka/orrery
#   file engine/orrery_loop/gate.py, line 41
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re

_ANSI_RE = re.compile(r"\x1b\[[0-9;]*m")


def strip_ansi(text: str | None) -> str:
    """Strip ANSI color/style escapes; ``None`` -> ``""`` (mirrors the PS null guard)."""
    if text is None:
        return ""
    return _ANSI_RE.sub("", text)
