# reduce_sampling_ratio
#
# Copied verbatim from https://github.com/xdas-dev/xdas
#   file xdas/coordinates/core.py, line 1504
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def reduce_sampling_ratio(numerator, denominator, dtype):
    """
    Reduce an already-typed ``(numerator, denominator)`` pair to lowest terms.

    Assumes `numerator` already carries a numpy scalar of the right dtype (see
    :func:`parse_scalar_delta`) and `denominator` is a strictly positive ``int``;
    callers are responsible for validating both before calling this. gcd-reduces
    exact dtypes (timedelta64 and integer); float dtypes have no tick, so the
    denominator is coerced to 1 -- an enforced invariant, dividing first.

    Datetime numerators are also normalised to `dtype`'s own resolution, so an
    in-memory coordinate matches the one read back after serialisation (which
    always encodes timedeltas at the coordinate's own datetime resolution).

    Returns
    -------
    numerator : numpy scalar
    denominator : numpy.int64
    """
    # Dispatch on `numerator`'s own dtype rather than `dtype`: a coordinate read
    # back from the pre-CF on-disk spelling can carry a numeric `tie_values`
    # paired with a timedelta64 rate (see `SampledCoordinate._collect_from_dataset`),
    # and that mismatch must round-trip unreduced rather than be forced into a
    # kind it never claimed.
    numerator_dtype = np.asarray(numerator).dtype
    if np.issubdtype(numerator_dtype, np.floating):
        if denominator != 1:
            numerator = numerator / denominator
        return numerator, np.int64(1)

    if np.issubdtype(numerator_dtype, np.timedelta64):
        # Align to the coordinate's own resolution only when it too is
        # datetime64-flavoured; the legacy mismatch above keeps its own unit.
        if np.issubdtype(dtype, np.datetime64):
            unit = np.datetime_data(dtype)[0]
            numerator = numerator.astype(f"timedelta64[{unit}]")
        else:
            unit = np.datetime_data(numerator_dtype)[0]
        ticks = int(numerator.view("i8"))
        g = int(np.gcd(abs(ticks), denominator)) or 1
        numerator = np.timedelta64(ticks // g, unit)
    else:
        ticks = int(numerator)
        g = int(np.gcd(abs(ticks), denominator)) or 1
        numerator = numerator_dtype.type(ticks // g)
    denominator //= g
    return numerator, np.int64(denominator)
