# simplify_hex
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/color.py, line 282
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def simplify_hex(s):
    '''
    Simplifiy a hex color code if possible

    E.g.:
        - #ffffffff -> #fff
        - #11aabbff -> #1ab

    :param s: hex color string
    :type s: str

    :return: simplified hex color string
    :rtype: str
    '''

    if s[1] == s[2] and s[3] == s[4] and s[5] == s[6] \
            and (len(s) == 9 and s[7] == s[8]):

        s = s[0] + s[1] + s[3] + s[5] + (s[7] if len(s) == 9 else '')

    if len(s) == 9 and s[-2:].lower() == 'ff':
        s = s[:7]

    elif len(s) == 5 and s[-1:].lower() == 'f':
        s = s[:4]

    return s
