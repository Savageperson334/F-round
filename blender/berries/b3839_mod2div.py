# mod2div
#
# Copied verbatim from https://github.com/trickv/traintap
#   file traintap/frame.py, line 60
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sensors and telemetry
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def xor(a: str, b: str) -> str:
    return "".join("0" if a[i] == b[i] else "1" for i in range(len(b)))


def mod2div(dividend: str, divisor: str) -> str:
    """Modulo-2 (carryless) division; returns the remainder string."""
    pick = len(divisor)
    tmp = dividend[0:pick]
    while pick < len(dividend):
        if tmp[0] == "1":
            tmp = xor(divisor[1:], tmp[1:]) + dividend[pick]
        else:
            tmp = xor(("0" * pick)[1:], tmp[1:]) + dividend[pick]
        pick += 1
    if tmp[0] == "1":
        tmp = xor(divisor[1:], tmp[1:])
    else:
        tmp = xor(("0" * pick)[1:], tmp[1:])
    return tmp
