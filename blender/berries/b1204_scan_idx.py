# scan_idx
#
# Copied verbatim from https://github.com/brodeau/gonzag
#   file gonzag/utils.py, line 206
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def scan_idx( vt, rt1, rt2 ):
    '''
    # Finding indices when we can start and stop when scanning the track file:
    # * vt: vector containing dates as Epoch UNIX time [float]
    # * rt1, rt2: the 2 dates of interest (first and last) [float]
    # RETURNS: the two corresponding position indices 
    '''
    nt = len(vt)
    for kt1 in range(  0, nt-1):
        if  (vt[kt1] <= rt1) and (vt[kt1+1] > rt1): break
    for kt2 in range(kt1, nt-1):
         if (vt[kt2] <= rt2) and (vt[kt2+1] > rt2): break
    kt2 = kt2 + 1
    return kt1, kt2
