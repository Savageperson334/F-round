# join
#
# Copied verbatim from https://github.com/Reytian/fm1-min1
#   file tools/manual_html.py, line 121
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re

CJK = re.compile(r"[　-〿㐀-鿿＀-￯]")


def join(a, b):
    """two lines of one paragraph: a space between them, but none between Chinese characters (a browser
    shows the line break there as a space)"""
    a, b = a.rstrip(), b.strip()
    return a + b if a and b and CJK.match(a[-1]) and CJK.match(b[0]) else f"{a} {b}".strip()
