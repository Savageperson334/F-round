# efuse_write_reg_addr
#
# Copied verbatim from https://github.com/magicshifter/ms4000
#   file tools/esptool/espefuse.py, line 120
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

EFUSE_REG_WRITE = [0x3FF5A01C, 0x3FF5A098, 0x3FF5A0B8, 0x3FF5A0D8]


def efuse_write_reg_addr(block, word):
    """
    Return the physical address of the efuse write data register
    block X word X.
    """
    return EFUSE_REG_WRITE[block] + (4 * word)
