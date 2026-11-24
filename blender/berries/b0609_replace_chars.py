# replace_chars
#
# Copied verbatim from https://github.com/OPM/opm-geochemistry
#   file pyGeoChem/pyGeoChem/io_cpp_solver/util.py, line 19
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def replace_chars(name, chars=[" ", "/","Å", "Ø", "Æ"], new_chars=["_","_","AA","O","AE"]):
    ''' replace Norwegian characters and space in names'''
    new_name = name
    for ch,nch in zip(chars,new_chars):
        new_name = new_name.replace(ch, nch)
    return new_name
