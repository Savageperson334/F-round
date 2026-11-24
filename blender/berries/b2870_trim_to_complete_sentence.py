# trim_to_complete_sentence
#
# Copied verbatim from https://github.com/nthmost/artery-thermal
#   file experience_generator/adams_markov_code/orig_chatgpt_markov.py, line 26
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Physical art output, plotters, paper and textile machines
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def trim_to_complete_sentence(story):
    # Use regex to find the last sentence boundary
    match = re.search(r'([.!?])\s', story[::-1])
    if match:
        # Return the story up to the last complete sentence
        return story[:-(match.start() + 1)]
    else:
        # If no sentence boundary is found, return the original story
        return story
