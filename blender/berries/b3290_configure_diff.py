# configure_diff
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/fomosto/elastic10_to_rotational8.py, line 23
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def almost_equal(a, b, eps):
    return abs(a - b < eps)


def configure_diff(x, xmin, xmax, dx):
    if almost_equal(x, xmin, 1e-6*dx):
        return dx, 0.
    elif almost_equal(x, xmax, 1e-6*dx):
        return 0., dx
    else:
        return dx, dx
