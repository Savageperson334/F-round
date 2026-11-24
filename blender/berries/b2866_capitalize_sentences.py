# capitalize_sentences
#
# Copied verbatim from https://github.com/nthmost/artery-thermal
#   file experience_generator/utils.py, line 3
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Physical art output, plotters, paper and textile machines
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def capitalize_sentences(text):
    # Split the text into sentences based on common sentence-ending punctuation
    sentences = re.split('(?<=[.!?]) +', text)

    # Capitalize the first letter of each sentence
    capitalized_sentences = [sentence.capitalize() for sentence in sentences]

    # Join the sentences back into a single string
    return ' '.join(capitalized_sentences)
