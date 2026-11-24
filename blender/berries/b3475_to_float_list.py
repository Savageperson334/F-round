# to_float_list
#
# Copied verbatim from https://github.com/pysmo/pysmo
#   file src/pysmo/lib/converters.py, line 85
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def to_float_list(value: list[float]) -> list[float]:
    """Convert an iterable of numbers to a list of `float` values."""
    return [float(item) for item in value]
