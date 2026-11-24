# to_sync_url
#
# Copied verbatim from https://github.com/BAHALLA/orrery
#   file core/orrery_core/persistence/db.py, line 62
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def to_sync_url(url: str) -> str:
    """Normalize an async PostgreSQL URL to its sync-driver equivalent.

    The reachability probe uses a synchronous engine, so the async ``+asyncpg``
    driver is swapped for ``+psycopg2``. This lets callers pass the very same
    URL used for the async session store.
    """
    async_prefix, sync_prefix = "postgresql+asyncpg", "postgresql+psycopg2"
    if url.startswith(async_prefix):
        return sync_prefix + url[len(async_prefix) :]
    return url
