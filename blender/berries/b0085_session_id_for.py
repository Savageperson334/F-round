# session_id_for
#
# Copied verbatim from https://github.com/BAHALLA/orrery
#   file agents/google-chat-bot/google_chat_bot/handler.py, line 173
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def session_id_for(space_name: str, thread_name: str | None) -> str:
    """Deterministic session id for a Chat thread (or space, for unthreaded posts).

    Deterministic rather than remembered, so the id survives a restart and every
    replica derives the same one — Pub/Sub delivery gives no guarantee about which
    replica handles which turn.

    Sessions are still **per participant**, not per thread: ADK scopes every
    session by ``(app_name, user_id, session_id)``, so two people in one thread
    sharing this id get two separate sessions behind it, each with its own
    history. That is the safe default (nobody reads a colleague's transcript) but
    it does mean the agent does not follow a thread across speakers — a
    coordinated multi-person thread needs shared state (``app:``-scoped keys or
    long-term memory), not a shared session id.
    """
    return f"gchat:{thread_name or space_name}"
