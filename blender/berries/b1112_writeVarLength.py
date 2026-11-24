# writeVarLength
#
# Copied verbatim from https://github.com/awalmer/Sonification-Exercises
#   file NYC Evictions/Jupyter/MidiFile.py, line 1723
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Sound sonification
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def writeVarLength(i):
    '''
    Accept an integer, and serialize it as a MIDI file variable length quantity

    Some numbers in MTrk chunks are represented in a form called a variable-
    length quantity.  These numbers are represented in a sequence of bytes,
    each byte holding seven bits of the number, and ordered most significant
    bits first. All bytes in the sequence except the last have bit 7 set,
    and the last byte has bit 7 clear.  This form allows smaller numbers to
    be stored in fewer bytes.  For example, if the number is between 0 and
    127, it is thus represented exactly as one byte.  A number between 128
    and 16383 uses two bytes, and so on.

    Examples:
    Number  VLQ
    128     81 00
    8192    C0 00
    16383   FF 7F
    16384   81 80 00
    '''
    if i == 0:
        return [0]

    vlbytes = []
    hibit = 0x00  # low-order byte has high bit cleared.
    while i > 0:
        vlbytes.append(((i & 0x7f) | hibit) & 0xff)
        i >>= 7
        hibit = 0x80
    vlbytes.reverse()  # put most-significant byte first, least significant last
    return vlbytes
