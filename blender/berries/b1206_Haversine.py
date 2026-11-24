# Haversine
#
# Copied verbatim from https://github.com/brodeau/gonzag
#   file gonzag/utils.py, line 296
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from math import cos
import numpy as nmp
from math import pi


def Haversine( plat, plon, xlat, xlon ):
    '''
    # ! VECTOR VERSION !
    # Returns the distance in km at the surface of the earth
    # between two GPS points (degreesN, degreesE)
    # (plat,plon)  : a point
    # xlat, xlon : 2D arrays
    #
    # Here we do not need accuracy on Earth radius, since the call
    # to this function is suposely made to find nearest point
    '''
    to_rad = pi/180.
    #
    #R = RadiusEarth( plat ) ; # it's the target location that matters...
    R = 6360.
    #
    a1 = nmp.sin( 0.5 * ((xlat - plat)*to_rad) )
    a2 = nmp.sin( 0.5 * ((xlon - plon)*to_rad) )
    a3 = nmp.cos( xlat*to_rad ) * cos(plat*to_rad)
    #
    return 2.*R*nmp.arcsin( nmp.sqrt( a1*a1 + a3 * a2*a2 ) )
