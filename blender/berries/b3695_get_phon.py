# get_phon
#
# Copied verbatim from https://github.com/suralmasha/RuTranscript
#   file src/ru_transcript/tools/allophones_tools.py, line 10
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Languages scripts and morphology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def get_phon(segment: list[str], i: int) -> str:
    """
    ...

    param segment:
    param i:
    return:
    """
    try:
        phon = segment[i]
    except IndexError:
        phon = ''

    return phon
