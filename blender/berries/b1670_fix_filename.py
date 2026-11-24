# fix_filename
#
# Copied verbatim from https://github.com/earthspecies/alp-data
#   file scripts/data_preprocessing_scripts/format_corvid_wascher.py, line 36
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Animal acoustics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def fix_filename(x: str) -> str:
    """
    fix filename differences between metadata and what's actually there

    Returns
    -----
    str fixed filename
    """
    if "35/a19.mp3" in x:
        x = x.replace("35/a19.mp3", "35_a19.mp3")
    if "2083/b08.mp3" in x:
        x = x.replace("2083/b08.mp3", "2083_b08.mp3")
    if ("[" in x) and ("]" in x):
        x = x.replace("[", "")
        x = x.replace("]", "")
    return x
