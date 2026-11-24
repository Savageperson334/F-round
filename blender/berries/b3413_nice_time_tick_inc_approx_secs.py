# nice_time_tick_inc_approx_secs
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/plot/__init__.py, line 741
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

hours = 3600.

days = hours*24

approx_years = days*365

approx_months = days*30.5

nice_time_tinc_inc_approx_units = {
    'seconds': 1,
    'months': approx_months,
    'years': approx_years}


def nice_value(x):
    '''
    Round x to nice value.
    '''

    if x == 0.0:
        return 0.0

    exp = 1.0
    sign = 1
    if x < 0.0:
        x = -x
        sign = -1
    while x >= 1.0:
        x /= 10.0
        exp *= 10.0
    while x < 0.1:
        x *= 10.0
        exp /= 10.0

    if x >= 0.75:
        return sign * 1.0 * exp
    if x >= 0.35:
        return sign * 0.5 * exp
    if x >= 0.15:
        return sign * 0.2 * exp

    return sign * 0.1 * exp


def nice_time_tick_inc(tinc_approx):

    if tinc_approx >= approx_years:
        return max(1.0, nice_value(tinc_approx / approx_years)), 'years'

    elif tinc_approx >= approx_months:
        nice = [1, 2, 3, 6]
        for tinc in nice:
            if tinc*approx_months >= tinc_approx or tinc == nice[-1]:
                return tinc, 'months'

    elif tinc_approx > days:
        return nice_value(tinc_approx / days) * days, 'seconds'

    elif tinc_approx >= 1.0:
        nice = [
            1., 2., 5., 10., 20., 30., 60., 120., 300., 600., 1200., 1800.,
            1*hours, 2*hours, 3*hours, 6*hours, 12*hours, days, 2*days]

        for tinc in nice:
            if tinc >= tinc_approx or tinc == nice[-1]:
                return tinc, 'seconds'

    else:
        return nice_value(tinc_approx), 'seconds'


def nice_time_tick_inc_approx_secs(tinc_approx):
    v, unit = nice_time_tick_inc(tinc_approx)
    return v * nice_time_tinc_inc_approx_units[unit]
