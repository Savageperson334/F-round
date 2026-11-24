# gform
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/util.py, line 2426
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def gform(number, significant_digits=3):
    '''
    Pretty print floating point numbers.

    Align floating point numbers at the decimal dot.

    ::

      |  -d.dde+xxx|
      |  -d.dde+xx |
      |-ddd.       |
      | -dd.d      |
      |  -d.dd     |
      |  -0.ddd    |
      |  -0.0ddd   |
      |  -0.00ddd  |
      |  -d.dde-xx |
      |  -d.dde-xxx|
      |         nan|


    The formatted string has length ``significant_digits * 2 + 6``.
    '''

    no_exp_range = (pow(10., -1),
                    pow(10., significant_digits))
    width = significant_digits+significant_digits-1+1+1+5

    if (no_exp_range[0] <= abs(number) < no_exp_range[1]) or number == 0.:
        s = ('%#.*g' % (significant_digits, number)).rstrip('0')
    else:
        s = '%.*E' % (significant_digits-1, number)
    s = (' '*(-s.find('.')+(significant_digits+1))+s).ljust(width)
    if s.strip().lower() == 'nan':
        s = 'nan'.rjust(width)
    return s
