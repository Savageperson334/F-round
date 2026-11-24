# get_sample_rate_prefix
#
# Copied verbatim from https://github.com/earthspecies/alp-data
#   file scripts/resample_datasets.py, line 497
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Animal acoustics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def get_sample_rate_prefix(target_sr: int) -> str:
    """Get the folder prefix for a given sample rate.

    Parameters
    ----------
    target_sr : int
        Target sample rate in Hz.

    Returns
    -------
    str
        Folder prefix like '16KHz' or '32KHz'.
    """
    if target_sr % 1000 != 0:
        # Use Hz for non-standard rates
        return f"{target_sr}Hz"
    return f"{target_sr // 1000}KHz"
