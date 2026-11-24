# remap_controls
#
# Copied verbatim from https://github.com/etcetc000/kitbasher
#   file examples/noise-plethora/authoring.py, line 248
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re

CONTROL_SLOTS={1:3,2:4,3:5,4:1,6:6,7:2}

DRIV_DEFAULT=0


def remap_controls(source):
    """Move the original control slots to the new layout. DRIV's slot is gone: its table lookups
    read entry DRIV_DEFAULT and the drive store disappears (unity drive needs no stage)."""
    source=source.replace('    move x0,y:(r6+$e)\n','')
    source,count=re.subn(r'    move y:\(r6\+\$5\),a\n    asr #16,a,a\n    move a1,a\n    add #>(\w+),a\n',
                         lambda m:f'    move #>{m[1]}+{DRIV_DEFAULT},a\n',source)
    assert count<=5, count  # DRIV-slot knob laws are constants already (lookup)
    assert not re.search(r'y:\(r6\+\$[58]\)',source)
    return re.sub(r'y:\(r6\+\$([1-8])\)',lambda m:f'y:(r6+${CONTROL_SLOTS[int(m[1])]})',source)
