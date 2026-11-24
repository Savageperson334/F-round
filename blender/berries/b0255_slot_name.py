# slot_name
#
# Copied verbatim from https://github.com/GRiMMBIENT/grimm
#   file tools/fm1_sample_upload.py, line 60
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def slot_name(s):
    """a slot's name: 8 characters (the header's, and what the FM-1 shows), A-Z 0-9 and a few signs; longer, its
    number at the end kept ("Sample-002" -> "SAMP-002"), else its start"""
    s = re.sub(r"[^A-Z0-9 _\-.#!+]", "", s.upper()).strip()
    if len(s) > 8:
        m = re.search(r"[ _\-.]?\d+$", s)
        tail = m.group(0) if m and len(m.group(0)) < 8 else ""
        s = s[:8 - len(tail)].rstrip() + tail
    return s or "SAMPLE"
