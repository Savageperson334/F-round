# clean_title
#
# Copied verbatim from https://github.com/simon0302010/shipwrecked-badge-meshtastic
#   file bin/generate_release_notes.py, line 186
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Shipwrecks and maritime ghosts
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def clean_title(title):
    """Clean up PR title for release notes."""
    # Remove common prefixes
    prefixes_to_remove = [
        r"^fix:\s*",
        r"^feat:\s*",
        r"^feature:\s*",
        r"^bug:\s*",
        r"^bugfix:\s*",
        r"^chore:\s*",
        r"^chore\([^)]+\):\s*",
        r"^refactor:\s*",
        r"^docs:\s*",
        r"^ci:\s*",
        r"^build:\s*",
        r"^perf:\s*",
        r"^style:\s*",
        r"^test:\s*",
    ]

    cleaned = title
    for prefix in prefixes_to_remove:
        cleaned = re.sub(prefix, "", cleaned, flags=re.IGNORECASE)

    # Ensure first letter is capitalized
    if cleaned:
        cleaned = cleaned[0].upper() + cleaned[1:]

    return cleaned.strip()
