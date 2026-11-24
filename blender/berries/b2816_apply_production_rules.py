# apply_production_rules
#
# Copied verbatim from https://github.com/mundyreimer/rewriting_systems
#   file intro_L_systems.py, line 44
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Artificial life, fluid mechanics, fields and emergence
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

DICT_OF_RULES = {}


def production_rule(sequence):
    '''
    Given a predecessor string
    Check if that string is in the dictionary of production rules
    Return the corresponding successor string, 
    Else return what you received
    '''
    # if predecessor string is in the dictionary
    if sequence in DICT_OF_RULES:
        # return the new successor string
        return DICT_OF_RULES[sequence]
    # else if it is not present, just return 
    # the predecessor string mapped to itself
    return sequence


def apply_production_rules(axiom, iterations):
    '''
    Given an initial string / axiom and amount of iterations
    Apply all the production rules to that list of symbols
    Return a new list of symbols
    '''
    # turn axiom string into a list of substrings
    # in our case, each of these substrings are 
    # an element of our list and each starts out
    # being a single character like F, +, -, etc
    list_of_substrings = [axiom]
    # for each iteration
    for _ in range(iterations):
        # start from the last substring in your list of substrings
        current_substring = list_of_substrings[-1]
        # for each character in that current substring, apply the production rule to it
        new_axiom = [production_rule(char) for char in current_substring]
        # add the new string to the list of substrings
        list_of_substrings.append(''.join(new_axiom))
    return list_of_substrings
