# flag_links
#
# Copied verbatim from https://github.com/movsim/traffic-simulation-de
#   file bash/engl2es.py, line 16
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Public transport and city motion
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def flag_links(html):
    """Use equally sized flag icons without changing language destinations."""
    def replace(match):
        block = match[0].replace(' style="display:block"', '')
        block = re.sub(r'>(?:Español|Espa&#241;ol)</a>', '><img src="figs/flagSpain.svg" alt="Espa&#241;ol" title="Espa&#241;ol" width="27%"></a>', block)
        block = block.replace('>Deutsch</a>', '><img src="figs/flagGerman.png" alt="Deutsch" title="Deutsch" width="27%"></a>')
        return block.replace('width="45%"', 'width="27%"')
    return re.sub(r'<div id="infoFlags"[^>]*>.*?</div>', replace, html, flags=re.S)
