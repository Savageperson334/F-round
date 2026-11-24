# classify_repository
#
# Copied verbatim from https://github.com/MargaretThomas/the-staged-awards
#   file skills/the-staged-awards/scripts/repository_profile.py, line 108
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def classify_repository(file_count: int, line_count: int) -> str:
    if file_count <= 100 and line_count <= 20_000:
        return "small"
    if file_count <= 500 and line_count <= 100_000:
        return "medium"
    return "large"
