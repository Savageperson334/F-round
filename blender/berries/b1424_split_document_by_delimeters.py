# split_document_by_delimeters
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/text/__init__.py, line 82
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def split_document_by_delimeters(string, regexp="[.,!?;: ]", min_word_len=1, stopwords=None):
    """
    :param string: input string (text document)
    :return: list of words
    """
    string = re.sub(r"(-\n)", "", string.lower())
    string = re.sub(r"(\n)", " ", string)
    words = re.split(regexp, string)

    if not stopwords:
        stopwords = []

    return [word for word in words if len(word) > min_word_len and word not in stopwords]
