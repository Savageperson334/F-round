# GridAngle
#
# Copied verbatim from https://github.com/brodeau/gonzag
#   file gonzag/utils.py, line 226
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from math import atan2
from math import cos
import numpy as nmp
from math import pi
from math import sin
from math import sqrt
from math import tan


def GridAngle( xlat, xlon ):
    ''' To be used with a NEMO ORCA-type of grid, to get an idea of the local distortion (rotation)
    #   of the grid
    # Returns local distortion of the grid in degrees [-180,180]
    '''
    to_rad = pi/180.
    pio4   = pi/4.
    (Ny,Nx) = nmp.shape(xlat)
    #
    angle = nmp.zeros((Ny,Nx))
    for ji in range(Nx):
        for jj in range(1,Ny-1):

            if abs( xlon[jj+1,ji]%360. - xlon[jj-1,ji]% 360. ) < 1.e-8:
                sint = 0.
                cost = 1.
                #
            else:
                zt0 = tan( pio4 - to_rad*xlat[jj,ji]/2. )
                # North pole direction & modulous (at t-point)
                zxnpt = 0. - 2. * cos( to_rad*xlon[jj,ji] ) * zt0
                zynpt = 0. - 2. * sin( to_rad*xlon[jj,ji] ) * zt0
                znnpt            = zxnpt*zxnpt + zynpt*zynpt
                #
                # j-direction: v-point segment direction (around t-point)
                zt1 = tan( pio4 - to_rad*xlat[jj+1,ji]/2. )
                zt2 = tan( pio4 - to_rad*xlat[jj-1,ji]/2. )
                zxvvt =  2.*( cos(to_rad*xlon[jj+1,ji])*zt1 - cos(to_rad*xlon[jj-1,ji])*zt2 )
                zyvvt =  2.*( sin(to_rad*xlon[jj+1,ji])*zt1 - sin(to_rad*xlon[jj-1,ji])*zt2 )
                znvvt = sqrt( znnpt * ( zxvvt*zxvvt + zyvvt*zyvvt )  )
                znvvt = max( znvvt, 1.e-12 )
                #
                sint = ( zxnpt*zyvvt - zynpt*zxvvt ) / znvvt
                cost = ( zxnpt*zxvvt + zynpt*zyvvt ) / znvvt
                angle[jj,ji] = atan2( sint, cost ) * 180./pi
        #
    return angle[:,:]
