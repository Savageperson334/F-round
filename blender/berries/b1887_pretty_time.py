# pretty_time
#
# Copied verbatim from https://github.com/fogleman/axi
#   file axi/progress.py, line 4
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Plotters & drawing machines
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def pretty_time(seconds):
    seconds = int(round(seconds))
    s = seconds % 60
    m = (seconds / 60) % 60
    h = (seconds / 3600)
    return '%d:%02d:%02d' % (h, m, s)
