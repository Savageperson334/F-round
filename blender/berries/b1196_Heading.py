# Heading
#
# Copied verbatim from https://github.com/brodeau/gonzag
#   file gonzag/bilin_mapping.py, line 16
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from math import atan2
from math import log
from math import pi
from math import radians
from math import tan


def Heading( plata,plona, platb,plonb ):
    '''
    #   ** Purpose: Compute true heading between point a and b
    #
    #   ** Method : suppose that the 2 points are not too far away from each other
    #               so that heading can be computed with loxodromy
    #
    #      "heading" is the angle (in degrees) that going from point A to point B makes:
    #                 IN A CLOCK-WISE FASHION !!!
    #               * 100% northward =>   0 deg.
    #               * 100% eastward  =>  90 deg.
    #               * 100% southward => 180 deg.
    #
    #  * history:
    #         J.M. Molines for SOSIE, may 2007
    #--------------------------------------------------------------
    '''
    repsilon = 1.E-9
    # There is a problem if the Greenwich meridian is between a and b
    xa = radians(plona)
    xb = radians(plonb)
    rr = max(abs(tan(pi/4.-radians(plata)/2.)), repsilon)  #lolo just to avoid FPE sometimes
    ya = -log(rr)
    rr = max(abs(tan(pi/4.-radians(platb)/2.)), repsilon)  #lolo just to avoid FPE sometimes
    yb = -log(rr)
    xb_xa=(xb-xa)%(2*pi)
    if  xb_xa >=  pi: xb_xa = xb_xa -2*pi
    if  xb_xa <= -pi: xb_xa = xb_xa +2*pi
    angled = atan2(xb_xa, yb - ya)
    rhdg = ( angled*180./pi ) % 360.
    #
    return rhdg
