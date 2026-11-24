# strip_module
#
# Copied verbatim from https://github.com/FartyPants/fm1-nachtfahrt
#   file web/make_site.py, line 27
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#   the same function also appears in: Reytian/fm1-min1, genkigenki/Speak37, isod89/clipper-fm1, isod89/clipper-pro, kpalaniuk/gnomad-firmware
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def strip_module(src):
    src = re.sub(r"^export\s+", "", src, flags=re.M)
    return re.sub(r"^import .*?;\n", "", src, flags=re.M)
