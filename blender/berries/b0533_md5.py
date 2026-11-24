# md5
#
# Copied verbatim from https://github.com/MikeChongCan/AITK
#   file aitk/utils/common.py, line 52
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import hashlib


def md5(value):
    m = hashlib.md5()
    m.update(value.encode('utf-8'))
    return m.hexdigest()
