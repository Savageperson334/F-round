# getImgDir
#
# Copied verbatim from https://github.com/ardamavi/HandwritingRecognition
#   file img_procedure.py, line 22
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def getImgDir(argumans):
    # We get the image directory:
    if len(argumans) < 2:
        return None
    return argumans[1]
