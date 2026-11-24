# createPem
#
# Copied verbatim from https://github.com/MercuryWorkshop/shipwrecked-pcb
#   file announcement-sender/ellipticcurve/utils/pem.py, line 9
#   licence (as GitHub reports it): Unlicense   see ../licenses/
#   catalogue shelf: Shipwrecks and maritime ghosts
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def createPem(content, template):
    lines = [
        content[start:start + 64]
        for start in range(0, len(content), 64)
    ]
    return template.format(content="\n".join(lines))
