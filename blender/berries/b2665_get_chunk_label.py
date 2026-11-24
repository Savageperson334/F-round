# get_chunk_label
#
# Copied verbatim from https://github.com/mbari-org/humpback-whale-song-detection
#   file hwsd/apply_model_day.py, line 16
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Animal surveillance, plants and living-world computation
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def get_chunk_label(tot_minutes: int) -> str:
    """Returns a readable elapsed time."""
    hours, minutes = divmod(tot_minutes, 60)
    return f"{hours:02}h:{minutes:02}m"
