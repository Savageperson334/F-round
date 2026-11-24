# cut_short_text
#
# Copied verbatim from https://github.com/BAHALLA/orrery
#   file agents/google-chat-bot/google_chat_bot/handler.py, line 77
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def cut_short_text(mutations: list[str], reason: str) -> str:
    """What to tell the thread when a turn was stopped mid-way.

    The one fact the reader cannot reconstruct is what already went through:
    asking again without knowing it is how a scale or a restart happens twice.
    """
    why = (
        "I ran out of time on this one and stopped mid-way."
        if reason == "timeout"
        else "I was restarted while working on this and stopped mid-way."
    )
    lines = [f"⚠️ *{why}* Nothing is still running, and I will not retry it on my own."]
    if mutations:
        steps = "\n".join(f"• `{tool}`" for tool in dict.fromkeys(mutations))
        lines.append(
            "*Changes that went through (or may have) before I stopped:*\n"
            f"{steps}\n\nCheck those before asking again, so nothing is done twice."
        )
    else:
        lines.append("Nothing was changed — it stopped while still reading.")
    lines.append("Ask again (ideally narrower) and I will pick it up from there.")
    return "\n\n".join(lines)
