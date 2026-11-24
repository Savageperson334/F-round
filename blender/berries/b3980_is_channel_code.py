# is_channel_code
#
# Copied verbatim from https://github.com/xdas-dev/xdas
#   file xdas/atoms/ml.py, line 403
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

CHANNEL_CODE_LENGTHS = (1, 3)


def is_channel_code(key):
    """
    Whether *key* has the shape of a channel code.

    True for a three-character SEED code (band, instrument, orientation) and
    for a bare orientation letter, false for anything longer, for a purely
    numeric key, and for a non-string one.

    Parameters
    ----------
    key : object
        A key of a collection level.

    Returns
    -------
    bool
        Whether *key* may be read as a channel code.

    Examples
    --------
    >>> from xdas.atoms.ml import is_channel_code
    >>> [is_channel_code(key) for key in ("SHZ", "Z", "STA1", "S-Z", "2", 2)]
    [True, True, False, False, False, False]
    """
    return (
        isinstance(key, str)
        and len(key) in CHANNEL_CODE_LENGTHS
        and key.isalnum()
        and not key.isdigit()
    )
