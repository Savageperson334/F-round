# clip
#
# Copied verbatim from https://github.com/JeremyPorquez/CRASHyperspectralAnalysis
#   file HSA/pyqtgraph/Point.py, line 11
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Microscopy & small worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def clip(x, mn, mx):
    if x > mx:
        return mx
    if x < mn:
        return mn
    return x
