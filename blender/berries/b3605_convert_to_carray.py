# convert_to_carray
#
# Copied verbatim from https://github.com/simon0302010/shipwrecked-badge-meshtastic
#   file bin/uf2conv.py, line 96
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Shipwrecks and maritime ghosts
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def convert_to_carray(file_content):
    outp = "const unsigned char bindata[] __attribute__((aligned(16))) = {"
    for i in range(len(file_content)):
        if i % 16 == 0:
            outp += "\n"
        outp += "0x%02x, " % ord(file_content[i])
    outp += "\n};\n"
    return outp
