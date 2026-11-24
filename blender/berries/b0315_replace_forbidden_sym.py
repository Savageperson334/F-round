# replace_forbidden_sym
#
# Copied verbatim from https://github.com/HuberTRoy/MusicBox
#   file MusicPlayer/features/configDownloadFrameFeatures.py, line 43
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Mechanical music boxes and organs
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def replace_forbidden_sym(string):

    return re.sub(r'[\\/:*?"<>|]{1}', ' ', string)
