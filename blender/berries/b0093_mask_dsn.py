# mask_dsn
#
# Copied verbatim from https://github.com/BAHALLA/orrery
#   file core/orrery_core/observability/log.py, line 33
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re

_DSN_PASSWORD_RE = re.compile(r"(://[^:/@\s]+:)[^@\s]+(@)")


def mask_dsn(url: str) -> str:
    """Return a database URL with the password segment redacted.

    Used when logging connection strings so credentials never land in
    log aggregators. Safe to call on URLs that have no password (no-op),
    on non-URL strings (no-op), and on URLs with unusual characters.

    >>> mask_dsn("postgresql+asyncpg://alice:s3cret@db:5432/agents")
    'postgresql+asyncpg://alice:[REDACTED]@db:5432/agents'
    >>> mask_dsn("postgresql://db:5432/agents")
    'postgresql://db:5432/agents'
    """
    return _DSN_PASSWORD_RE.sub(r"\1[REDACTED]\2", url)
