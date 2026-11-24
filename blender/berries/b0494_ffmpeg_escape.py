# ffmpeg_escape
#
# Copied verbatim from https://github.com/MargaretThomas/the-staged-awards
#   file skills/the-staged-awards/scripts/compose_awards_image.py, line 18
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def ffmpeg_escape(value: str) -> str:
    """Escape a path for use as an FFmpeg filter value."""
    return value.replace("\\", "\\\\").replace(":", "\\:").replace("'", "\\'")
