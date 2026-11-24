# human_size
#
# Copied verbatim from https://github.com/simon0302010/shipwrecked-badge-meshtastic
#   file bin/analyze_map.py, line 25
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Shipwrecks and maritime ghosts
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def human_size(num_bytes: int) -> str:
    """Return a friendly size string with one decimal place."""
    if num_bytes < 1024:
        return f"{num_bytes:,} B"
    num = float(num_bytes)
    for unit in ("KB", "MB", "GB"):
        num /= 1024.0
        if num < 1024.0:
            return f"{num:.1f} {unit}"
    return f"{num:.1f} TB"
