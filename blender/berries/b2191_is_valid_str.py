# is_valid_str
#
# Copied verbatim from https://github.com/huyhoang17/CRNN_CTC_English_Handwriting_Recognition
#   file src/data_generator.py, line 60
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#   the same function also appears in: huyhoang17/Vietnamese_Handwriting_Recognition
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def is_valid_str(letters, s):
    for ch in s:
        if ch not in letters:
            return False
    return True
