# to_strict_int
#
# Copied verbatim from https://github.com/pysmo/pysmo
#   file src/pysmo/lib/converters.py, line 90
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def to_strict_int(value: int) -> int:
    """Convert `value` to `int`, raising if it isn't a whole number.

    Unlike a bare `int()` converter, this rejects a fractional value (e.g.
    `2.5`) instead of silently discarding its fractional part.
    """
    as_float = float(value)
    if not as_float.is_integer():
        raise ValueError(f"{value!r} is not a whole number.")
    return int(as_float)
