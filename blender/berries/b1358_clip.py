# clip
#
# Copied verbatim from https://github.com/chrisfulcher/orrery
#   file src/orrery/assess.py, line 171
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def clip(text: str | None, limit: int) -> str:
    """The head of ``text`` within ``limit`` characters, cut at a word and marked."""
    text = (text or "").strip()
    return text if len(text) <= limit else text[:limit].rsplit(" ", 1)[0] + " […]"
