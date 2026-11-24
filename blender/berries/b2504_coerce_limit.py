# coerce_limit
#
# Copied verbatim from https://github.com/kiyotakali/Miru
#   file companion.py, line 11
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Obscure computers, languages, unusual interfaces
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def coerce_limit(value, default=20, minimum=1, maximum=100):
    try:
        limit = int(value)
    except (TypeError, ValueError):
        limit = default
    return max(minimum, min(limit, maximum))
