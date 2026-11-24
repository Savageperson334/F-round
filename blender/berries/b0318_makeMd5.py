# makeMd5
#
# Copied verbatim from https://github.com/HuberTRoy/MusicBox
#   file MusicPlayer/widgets/base.py, line 72
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Mechanical music boxes and organs
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import hashlib


def makeMd5(raw):

     m = hashlib.md5()  
     m.update(raw.encode()) 
     return  m.hexdigest()
