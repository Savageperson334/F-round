# dict_to_string
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/fomosto/report/report_call.py, line 71
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def dict_to_string(dic):
    st = 4
    st2 = 20
    s = ''
    for k, v in dic.items():
        s += '\n{0}{1}{2}{3}'.format(' '*st, k, ' '*(st2 - st - len(k)), v)
    return s
