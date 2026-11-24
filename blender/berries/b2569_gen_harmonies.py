# gen_harmonies
#
# Copied verbatim from https://github.com/linev8k/sonnify
#   file pyo_callbacks.py, line 79
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Sound sonification
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def gen_harmonies(n_streams, base_freq=200, ratio=[1,4,5,6]):

    """Generate harmonies for as many streams as needed. Obviously limited by range of reasonable frequencies.
    Used during weights sonification.
    Args:
        base_freq: Basic frequency to build on.
        ratio: List with ratios for frequencies. Should start with 1.
        n_streams: Number of streams to build the harmonies for.
    """

    mul_base = 1
    n_ratio = len(ratio)-1

    all_harms = []

    for stream in range(n_streams+1):

        #add new octave harmonies when more streams are needed
        if stream % n_ratio == 0:

            #adjust frequency to be multiple of base frequency
            freq = base_freq * mul_base
            mul_base += 1

            #generate harmonies
            harms = [freq * ratio[i] / ratio[1] for i in range(1, len(ratio))]
            #print(harms)
            all_harms += harms

    #return as many streams as needed
    return all_harms[:n_streams]
