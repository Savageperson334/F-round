# defineReceiverPairs
#
# Copied verbatim from https://github.com/xaviermouy/ecosound
#   file ecosound/localization/archive/localizationlib.py, line 94
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Animal acoustics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def defineReceiverPairs (n_receivers, ref_receiver=0):
    Rpairs = []
    for i in range(n_receivers):
        if i != ref_receiver:
            pair = [ref_receiver, i]
            Rpairs.append(pair)
    return Rpairs
