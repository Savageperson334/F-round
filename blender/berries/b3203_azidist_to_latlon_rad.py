# azidist_to_latlon_rad
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/orthodrome.py, line 665
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math
import numpy as num

d2r = math.pi/180.

r2d = 1./d2r


def clip(x, mi, ma):
    '''
    Clip values of an array.

    :param x: Continunous data to be clipped.
    :param mi: Clip minimum.
    :param ma: Clip maximum.
    :type x: :py:class:`numpy.ndarray`
    :type mi: float
    :type ma: float

    :return: Clipped data.
    :rtype: :py:class:`numpy.ndarray`
    '''
    return num.minimum(num.maximum(mi, x), ma)


def wrap(x, mi, ma):
    '''
    Wrapping continuous data to fundamental phase values.

    .. math::
        x_{\\mathrm{wrapped}} = x_{\\mathrm{cont},i} -
            \\frac{ x_{\\mathrm{cont},i} - r_{\\mathrm{min}} }
                  { r_{\\mathrm{max}} -  r_{\\mathrm{min}}}
            \\cdot ( r_{\\mathrm{max}} -  r_{\\mathrm{min}}),\\quad
        x_{\\mathrm{wrapped}}\\; \\in
            \\;[ r_{\\mathrm{min}},\\, r_{\\mathrm{max}}].

    :param x: Continunous data to be wrapped.
    :param mi: Minimum value of wrapped data.
    :param ma: Maximum value of wrapped data.
    :type x: :py:class:`numpy.ndarray`
    :type mi: float
    :type ma: float

    :return: Wrapped data.
    :rtype: :py:class:`numpy.ndarray`
    '''
    return x - num.floor((x-mi)/(ma-mi)) * (ma-mi)


def azidist_to_latlon_rad(lat0, lon0, azimuth_rad, distance_rad):
    '''
    Absolute latitudes and longitudes are calculated from relative changes.

    For numerical stability a range between of ``-1.0`` and ``1.0`` is
    enforced for ``c`` and ``alpha``.

    .. math::

        \\Delta {\\bf a}_i \\; \\text{and} \\; \\Delta \\gamma_i \\;
            \\text{are relative distances and azimuths from lat0 and lon0 for
                \\textit{i} source points of a finite source.}

    .. math::

        \\mathrm{b} &= \\frac{\\pi}{2} -\\frac{\\pi}{180}\\;\\mathrm{lat_0}\\\\
        {\\bf c}_i &=\\arccos[\\; \\cos(\\Delta {\\bf{a}}_i)
            \\cos(\\mathrm{b}) + |\\Delta \\gamma_i| \\,
            \\sin(\\Delta {\\bf a}_i)
                \\sin(\\mathrm{b})\\; ] \\\\
        \\mathrm{lat}_i &=  \\frac{180}{\\pi}
                          \\left(\\frac{\\pi}{2} - {\\bf c}_i \\right)

    .. math::

         \\alpha_i &= \\arcsin \\left[ \\; \\frac{ \\sin(\\Delta {\\bf a}_i )
                         \\sin(|\\Delta \\gamma_i|)}{\\sin({\\bf c}_i)}\\;
                         \\right] \\\\
        \\alpha_i &= \\begin{cases}
                 \\alpha_i, &\\text{if}  \\; \\cos(\\Delta {\\bf a}_i) -
                 \\cos(\\mathrm{b}) \\cos({\\bf{c}}_i) > 0, \\;
                 \\text{else} \\\\
                 \\pi - \\alpha_i, & \\text{if} \\; \\alpha_i > 0,\\;
                 \\text{else}\\\\
                -\\pi - \\alpha_i, & \\text{if} \\; \\alpha_i < 0.
                \\end{cases} \\\\
        \\mathrm{lon}_i &=   \\mathrm{lon_0} +
             \\frac{180}{\\pi} \\,
             \\frac{\\Delta \\gamma_i }{|\\Delta \\gamma_i|}
                            \\cdot \\alpha_i
                             \\text{, with $\\alpha_i \\in [-\\pi,\\pi]$}

    :param lat0: Latitude origin of the cartesian coordinate system in [deg].
    :param lon0: Longitude origin of the cartesian coordinate system in [deg].
    :param distance_rad: Distances from origin in [rad].
    :param azimuth_rad: Azimuth from origin in [rad].
    :type distance_rad: :py:class:`numpy.ndarray`, ``(N)``
    :type azimuth_rad: :py:class:`numpy.ndarray`, ``(N)``
    :type lat0: float
    :type lon0: float

    :return: Array with latitudes and longitudes in [deg].
    :rtype: :py:class:`numpy.ndarray`, ``(2xN)``
    '''

    a = distance_rad
    gamma = azimuth_rad

    b = math.pi/2.-lat0*d2r

    alphasign = 1.
    alphasign = num.where(gamma < 0, -1., 1.)
    gamma = num.abs(gamma)

    c = num.arccos(clip(
        num.cos(a)*num.cos(b)+num.sin(a)*num.sin(b)*num.cos(gamma), -1., 1.))

    alpha = num.arcsin(clip(
        num.sin(a)*num.sin(gamma)/num.sin(c), -1., 1.))

    alpha = num.where(
        num.cos(a)-num.cos(b)*num.cos(c) < 0,
        num.where(alpha > 0,  math.pi-alpha, -math.pi-alpha),
        alpha)

    lat = r2d * (math.pi/2. - c)
    lon = wrap(lon0 + r2d*alpha*alphasign, -180., 180.)

    return lat, lon
