# get_speed
#
# Copied verbatim from https://github.com/isi-vista/VistaOCR
#   file src/calc_time.py, line 17
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def get_speed(w, benchmarking=True):
    if True:
        return 0.0012 * w + 0.01

    speed = { 100: 0.13,
              150: 0.19,
              200: 0.25,
              250: 0.31,
              300: 0.38,
              350: 0.43,
              400: 0.49,
              450: 0.55,
              500: 0.61,
              550: 0.67,
              600: 0.73
    }

    if w in speed:
        return speed[w]

    if w > 600:
        return (w/600 * 0.73)

    raise Exception("Haven't done this bit yet")
