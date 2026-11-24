# handle_dangling_clause
#
# Copied verbatim from https://github.com/nthmost/artery-thermal
#   file experience_generator/spacy_markov.py, line 38
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Physical art output, plotters, paper and textile machines
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def handle_dangling_clause(sentence, model):
    """Attempt to complete a sentence with a dangling clause."""
    if re.search(r'\b(and|or|but|because|if|that|which|when|where|while)\b[.!?]?$', sentence, re.I):
        additional_clause = model.make_sentence(tries=5)
        if additional_clause:
            return sentence + " " + additional_clause
    return sentence
