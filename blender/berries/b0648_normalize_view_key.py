# normalize_view_key
#
# Copied verbatim from https://github.com/Pouzor/homelable
#   file backend/app/services/inventory_sync.py, line 331
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def _is_current_service_key(key: str) -> bool:
    """Whether ``key`` is already written the way :func:`_service_view_key` writes one.

    A current key ends with the path, which is rendered anchored at ``/`` or
    empty; a legacy key ends with a service name. That is what keeps a
    pre-#469 ``port|protocol|name`` whose name happens to carry a ``|`` from
    reading as a current key — today's are escaped, so they never carry one.
    """
    parts = key.split("|")
    return len(parts) in (4, 5) and (parts[-1] == "" or parts[-1].startswith("/"))


def normalize_view_key(key: str, kind: str) -> str:
    """A stored view key in today's form.

    Views written before #469 address a service by ``port|protocol|name``. The
    name in one is a snapshot of what the service was called when the view was
    written, so a renamed service cannot be found by re-deriving it — the key
    has to be narrowed instead. A key that names a port drops everything after
    it; one that does not is port-less and keeps its name, as does every
    property key.

    A port-less service renders its absent port as ``None`` today, but a key
    written for one carrying ``""`` stored an empty segment instead. Both mean
    the same absent port, so the empty one is spelled the new way rather than
    left to miss.

    What comes back is the narrowest form the key itself can justify: a view
    written before #503 names no host and no path, and nothing here can invent
    the one it meant. :func:`apply_view` finishes the job against the row, which
    is the only place that knows what services there are to choose between.

    Applied on read, so a view migrates the next time its node is saved rather
    than needing a migration of its own.
    """
    if kind != "services" or _is_current_service_key(key):
        return key
    parts = key.split("|", 2)
    if len(parts) != 3:
        return key
    if parts[0] == "":
        return f"None|{parts[1]}|{parts[2]}"
    if parts[0] == "None":
        return key
    return f"{parts[0]}|{parts[1]}"
