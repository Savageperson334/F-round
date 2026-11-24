# tail_lines
#
# Copied verbatim from https://github.com/simon0302010/shipwrecked-badge-meshtastic
#   file mcp-server/src/meshtastic_mcp/pio.py, line 305
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Shipwrecks and maritime ghosts
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def tail_lines(text: str, n: int = 200) -> str:
    """Last `n` lines of `text`, joined with newlines. Empty string stays empty."""
    if not text:
        return ""
    lines = text.splitlines()
    return "\n".join(lines[-n:])
