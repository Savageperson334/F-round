# quoted
#
# Copied verbatim from https://github.com/c64cryptoboy/retro-archaeology-skills
#   file skills/pcode-disassembly/scripts/reconstruct/symbolic.py, line 36
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def quoted(data):
    """BASIC-like byte spelling, not the glyphs of a particular C64 charset."""
    parts=[];buf=''
    for b in data:
        # $5C, $5E, $5F and the $60 bank are not ASCII backslash, carets,
        # underscore, or lowercase text.  Keep only unambiguous source bytes.
        if (0x20<=b<=0x5B and b!=0x22) or b==0x5D:buf+=chr(b)
        else:
            if buf:parts.append('"'+buf+'"');buf=''
            parts.append(f'CHR$({b})')
    if buf:parts.append('"'+buf+'"')
    return '+'.join(parts) or '""'
