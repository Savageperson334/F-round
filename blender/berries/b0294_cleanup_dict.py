# cleanup_dict
#
# Copied verbatim from https://github.com/HendrikStrobelt/LSTMVis
#   file lstm_server.py, line 52
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import json


def cleanup_dict(old_dictionary):
    new_dictionary={}
    for key, val in old_dictionary.items():
        try:
            s=json.dumps(val)
            new_dictionary[key]=val
        except:
            if type(val) is dict:
                new_dictionary[key]=cleanup_dict(val)
            elif type(val) is type({}.keys()):
                new_dictionary[key]=list(val)
    return new_dictionary
