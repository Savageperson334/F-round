# gcd2
#
# Copied verbatim from https://github.com/magicshifter/ms4000
#   file tools/esptool/ecdsa/numbertheory.py, line 206
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def gcd2(a, b):
  """Greatest common divisor using Euclid's algorithm."""
  while a:
    a, b = b%a, a
  return b
