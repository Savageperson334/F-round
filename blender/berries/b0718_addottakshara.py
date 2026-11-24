# addottakshara
#
# Copied verbatim from https://github.com/SubhrajyotiSen/KannadaHandwritingRecognition
#   file Unicode/seqgen.py, line 33
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def addottakshara(myseq, ott):
    if(ott == 6):
        myseq = myseq + "+" + "6"
    elif(ott == 9):
        initial_vowel = int(myseq.rsplit('+')[-1])
        vowel_len = len(str(initial_vowel))
        print(vowel_len)
        myseq = myseq[0: len(myseq)-vowel_len]
        myseq = myseq + "9"
    elif('+' in myseq):
        letter = myseq.split('+')[0]
        vowel = myseq.split('+')[1]
        myseq = letter + "^" + str(ott)
        myseq = myseq + "+" + vowel
    else:
        myseq = myseq + "^" + str(ott)
    return myseq
