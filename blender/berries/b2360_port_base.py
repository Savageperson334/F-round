# port_base
#
# Copied verbatim from https://github.com/isod89/clipper-pro
#   file tools/fm1_install.py, line 482
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def port_base(n):
    """a port name without its in / out part ("MIDIIN2 (X)" / "MIDIOUT2 (X)", "X 1", "X In"), as web/fm1ota.js portBase"""
    n = re.sub(r"^MIDI(?:IN|OUT)(\d*) \((.*)\)$", r"\2 \1", n, flags=re.I)
    n = re.sub(r"\s+\d+$", "", n.strip())
    return re.sub(r"[ -](?:in|out|input|output)$", "", n, flags=re.I).strip().lower()
