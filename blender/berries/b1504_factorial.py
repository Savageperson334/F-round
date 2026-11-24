# factorial
#
# Copied verbatim from https://github.com/computational-imaging/hsplat
#   file hsplat/utils.py, line 377
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Optical computing and holograms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def factorial(n):
    """Compute the factorial of n."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
