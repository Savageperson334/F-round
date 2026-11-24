# spaces_from_env
#
# Copied verbatim from https://github.com/BAHALLA/orrery
#   file core/orrery_core/knowledge/sources/confluence.py, line 207
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def spaces_from_env(raw: str | None) -> list[str]:
    """Parse ``KNOWLEDGE_CONFLUENCE_SPACES`` — comma-separated keys."""
    return [space.strip() for space in (raw or "").split(",") if space.strip()]
