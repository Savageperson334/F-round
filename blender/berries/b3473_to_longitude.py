# to_longitude
#
# Copied verbatim from https://github.com/pysmo/pysmo
#   file src/pysmo/lib/converters.py, line 32
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def to_longitude(value: float | str) -> float:
    """Convert a value to a `float` longitude in degrees, folding -180 onto +180.

    -180 and +180 name the same meridian; +180 is kept as the single
    canonical value so two spellings of the antimeridian cannot compare
    unequal. Values genuinely outside `[-180, 180]` are returned unchanged
    for a downstream validator to reject.
    """
    longitude = float(value)
    return 180.0 if longitude == -180.0 else longitude
