# encode_delta
#
# Copied verbatim from https://github.com/xdas-dev/xdas
#   file xdas/coordinates/core.py, line 1751
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np

CODE_TO_UNITS = {
    "h": "hours",
    "m": "minutes",
    "s": "seconds",
    "ms": "milliseconds",
    "us": "microseconds",
    "ns": "nanoseconds",
}


def encode_delta(key, value):
    """Serialise a scalar (possibly timedelta64) into a dict of dataset attributes."""
    if value is None:
        return {}
    if np.issubdtype(np.asarray(value).dtype, np.timedelta64):
        code, count = np.datetime_data(value.dtype)
        if code == "generic":  # e.g. timedelta64(0); promote to nanoseconds
            value = value.astype("timedelta64[ns]")
            code, count = np.datetime_data(value.dtype)
        return {
            key: int(count * value.astype(int)),
            f"{key}_dtype": "timedelta64[ns]",
            f"{key}_units": CODE_TO_UNITS[code],
        }
    return {key: value}
