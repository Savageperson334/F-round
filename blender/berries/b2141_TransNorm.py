# TransNorm
#
# Copied verbatim from https://github.com/gvard/astrodata
#   file src/astrodata/solarsystem/deltav.py, line 260
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def NodeChoice(
    w: float, ec: float, a: float
) -> float:  # which node was chosen, for all future calculation the periapsis direction is defined as 0 degrees
    Node1 = a * (1 - (ec**2)) / (1 + ec * math.cos(-w))
    Node2 = a * (1 - (ec**2)) / (1 + ec * math.cos(math.pi - w))
    if Node1 > Node2:
        return -w
    else:
        return math.pi - w


def VecXTrans(w: float, i: float, ec: float, a: float) -> float:  # X direction vector component of transfer orbit at node
    return -math.sin(NodeChoice(w, ec, a)) * math.cos(i)


def VecYTrans(w: float, i: float, ec: float, a: float) -> float:  # Y direction vector component of transfer orbit at node
    return math.cos(NodeChoice(w, ec, a)) * math.cos(i)


def VecZTrans(i: float) -> float:
    return math.sin(i)


def TransNorm(w: float, i: float, ec: float, a: float) -> float:
    return math.sqrt(
        VecXTrans(w, i, ec, a) ** 2 + VecYTrans(w, i, ec, a) ** 2 + VecZTrans(i) ** 2
    )
