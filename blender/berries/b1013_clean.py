# clean
#
# Copied verbatim from https://github.com/alexbarakov/amsterdam-by-building
#   file pipeline/s09_residents.py, line 140
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Historic cartography
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def clean(wt):
    """Wikitext to plain sentences; headings become sentence breaks so a quote never spans sections."""
    wt = re.sub(r"<ref[^>]*/>|<ref[^>]*>.*?</ref>|<!--.*?-->", "", wt, flags=re.S)
    for _ in range(3):
        wt = re.sub(r"\{\{[^{}]*\}\}", "", wt)
    wt = re.sub(r"\[\[(?:Bestand|File|Afbeelding|Categorie|Image):[^\[\]]*(?:\[\[[^\]]*\]\][^\[\]]*)*\]\]", "", wt, flags=re.I)
    wt = re.sub(r"\[\[(?:[^|\]]*\|)?([^\]]*)\]\]", r"\1", wt)
    wt = re.sub(r"\[https?://\S+\s*([^\]]*)\]", r"\1", wt)
    wt = re.sub(r"^=+[^=\n]*=+\s*$", ". ", wt, flags=re.M)
    wt = re.sub(r"^[*#:;|!{].*$", ". ", wt, flags=re.M)
    wt = re.sub(r"<[^>]+>|'{2,}|thumb\|", "", wt)
    return re.sub(r"\s+", " ", wt)
