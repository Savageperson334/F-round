# replace_ending
#
# Copied verbatim from https://github.com/livingingroups/animal2vec
#   file animal2vec_inference.py, line 638
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Animal acoustics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def replace_ending(st, target_ending=".csv"):
    st_ = st
    supported_file_types = ["WAV", "AIFF", "AIFC", "FLAC", "OGG", "MP3", "MAT"]
    for ft in supported_file_types:
        regex_ft = "." + "".join(["[{}{}]".format(x.lower(), x.upper()) for x in ft])
        st_ = re.sub(regex_ft, "{}".format(target_ending), st_)
    return st_
