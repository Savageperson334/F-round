# segment_by_split
#
# Copied verbatim from https://github.com/MartinThoma/hwrt
#   file hwrt/utils.py, line 539
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def segment_by_split(split, recording):
    """

    Parameters
    ----------
    split : String of 0s and 1s
        For example "010".
    recording : list
        A recording of handwritten text.
    """
    segmented = [[recording[0]]]
    for i in range(len(recording) - 1):
        if split[i] == "1":
            segmented.append([])
        segmented[-1].append(recording[i + 1])
    assert split.count("1") + 1 == len(segmented), (
        f'split.count("1") + 1 = {split.count("1") + 1} != '
        f"{len(segmented)} = len(segmented)"
    )
    return segmented
