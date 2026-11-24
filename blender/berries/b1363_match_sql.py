# match_sql
#
# Copied verbatim from https://github.com/chrisfulcher/orrery
#   file src/orrery/naics.py, line 55
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def match_sql(column: str, param: str) -> str:
    """The SQL form of ``matches``: true when ``column`` starts with any element of the JSON
    array bound to ``param``. ``substr`` rather than ``LIKE`` so that no element of the slice
    can be read as a wildcard pattern. Callers keep their own null guard on ``param``."""
    return (
        f"EXISTS (SELECT 1 FROM json_each({param})"
        f" WHERE substr({column}, 1, length(value)) = value)"
    )
