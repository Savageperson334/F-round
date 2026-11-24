# slack_scope
#
# Copied verbatim from https://github.com/BAHALLA/orrery
#   file agents/slack-bot/slack_bot/confirmation.py, line 58
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def slack_scope(channel: str, thread_ts: str | None) -> tuple[str, str | None]:
    """``(scope_key, parent_scope)`` for a Slack channel/thread."""
    if thread_ts:
        return f"{channel}:{thread_ts}", channel
    return channel, None
