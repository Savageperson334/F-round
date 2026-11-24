# prop_dist_to_diopter
#
# Copied verbatim from https://github.com/computational-imaging/neural-3d-holography
#   file utils.py, line 329
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Optical computing and holograms
#   the same function also appears in: computational-imaging/time-multiplexed-neural-holography
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def prop_dist_to_diopter(prop_dists, focal_distance, prop_dist_inf, from_lens=True):
    """
    Calculates distance from the user in diopter unit given the propagation distance from the SLM.
    :param prop_dists:
    :param focal_distance:
    :param prop_dist_inf:
    :param from_lens:
    :return:
    """
    x0 = prop_dist_inf  # prop distance from SLM that correcponds to optical infinity from the user
    f = focal_distance  # focal distance of eyepiece

    if from_lens:  # distance is from the lens
        diopters = [1 / (x0 + f - x) - 1 / f for x in prop_dists]  # diopters from the user side
    else:  # distance is from the user (basically adding focal length)
        diopters = [(x - x0) / f**2 for x in prop_dists]

    return diopters
