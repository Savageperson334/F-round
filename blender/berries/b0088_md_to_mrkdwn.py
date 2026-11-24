# md_to_mrkdwn
#
# Copied verbatim from https://github.com/BAHALLA/orrery
#   file agents/slack-bot/slack_bot/formatting.py, line 11
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def _replace_outside_code(text: str, pattern: str, replacement: str) -> str:
    """Apply regex replacement only outside of code blocks."""
    parts = text.split("```")
    for i in range(0, len(parts), 2):  # even indices are outside code blocks
        parts[i] = re.sub(pattern, replacement, parts[i])
    return "```".join(parts)


def md_to_mrkdwn(text: str) -> str:
    """Convert common Markdown to Slack mrkdwn.

    Handles bold, italic, headings, and links.
    Code blocks (```) are left as-is since Slack supports them.
    """
    # Headings: ## Heading → *Heading*
    text = re.sub(r"^#{1,6}\s+(.+)$", r"*\1*", text, flags=re.MULTILINE)

    # Bold: **text** → *text*  (but skip inside code blocks)
    text = _replace_outside_code(text, r"\*\*(.+?)\*\*", r"*\1*")

    return text
