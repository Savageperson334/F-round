# magnitude_to_moment
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/moment_tensor.py, line 248
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def magnitude_to_moment(magnitude):
    '''
    Convert moment magnitude Mw to scalar moment.

    :param magnitude: moment magnitude
    :returns: scalar moment [Nm]

    See :py:func:`moment_to_magnitude`.
    '''

    return 10.0**(1.5*(magnitude+10.7))*1.0e-7
