# name_key
#
# Copied verbatim from https://github.com/Worldwave/Wakes
#   file tools/gen_engines.py, line 101
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def name_key(name):
    """How names are compared, here and on the device (sp1_cnfg.h, sp1_engine_name_eq):
    letters and digits only, case ignored -- so "grain / formant", "grain-formant" and
    "Grain Formant" are one engine, and a PRST file saved under an older spelling loads."""
    return "".join(ch for ch in name.lower() if ch.isascii() and ch.isalnum())
