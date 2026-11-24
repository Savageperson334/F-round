# verticalsplit
#
# Copied verbatim from https://github.com/anshdavid/Procedural-City-Generation
#   file procedural_city_generation/building_generation/building_tools.py, line 257
#   licence (as GitHub reports it): MPL-2.0   see ../licenses/
#   catalogue shelf: Procedural and generated worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def verticalsplit(buildingheight, floorheight):
    """
    Splits the Building vertically.

    Parameters
    ----------
    buildingheight  : float
        Height of the building
    floorheight  :  float
        Height of each floor

    Returns
    -------
    list<char>
        Each character stands for one "building element" where:
        l=ledge
        f=floor
        b=base (Erdgeschoss)
        r=roof
    """

    #List of chars to be returned. Starts with base
    returnlist=['b']

    #Finds maximum number of floors which fit in. -1 because the first floor is the base
    nfloors=int(buildingheight//floorheight)-1

    #Finds maximum amount of ledges
    rest=buildingheight%floorheight
    nledges=int(rest//(floorheight/10.))

    #If there is at least 1 ledge, create it after the basement
    if nledges>0:
        nledges-=1
        returnlist.append('l')

    #If there is 1 ledge left, create it at the very top and return returnlist.
    if nledges == 1:
        nledges-=1
        for i in range(nfloors):
            returnlist.append('f')
        returnlist.append('l')
        returnlist.append('r')
        return returnlist

    #Finds how many floors per ledge are to be created
    factor=np.inf
    if nledges>0:
        factor=int(nfloors//nledges)
    last=True

    i=0
    while nfloors>=0:
        returnlist.append('f')
        nfloors-=1
        i+=1
        #If index is multiple of factor, add a ledge
        if factor>0 and i%factor == 0 and factor<3:
            returnlist.append('l')
    if returnlist[-1]!='l':
        returnlist.append('l')
    returnlist.append('r')
    return returnlist
