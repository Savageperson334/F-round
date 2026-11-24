# fraction_derivative
#
# Copied verbatim from https://github.com/jlanversin/ONIX
#   file onix/nax/functions.py, line 805
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def fraction_derivative(concatenate_history_matrix, history_fluence, chain):

    fraction_derivative_dict = {}
    for j in range(len(chain)):
        data = chain[j]
        name = data[0]
        fraction_derivative = []
        fraction_evolution = concatenate_history_matrix[j]
        index = 0
        for i in range(len(fraction_evolution)-1):
            # if index in step_break_indexes:
            #   index += 1
            #   continue
            #derivative = abs((fraction_evolution[i+1]-fraction_evolution[i])/(history_fluence[i+1]-history_fluence[i]))
            derivative = (fraction_evolution[i+1]-fraction_evolution[i])/(history_fluence[i+1]-history_fluence[i])
            # print ('ratio diff',ratio_evolution[i+1]-ratio_evolution[i])
            # print ('fluence diff',(history_fluence[i+1]-history_fluence[i]))
            fraction_derivative.append(derivative)
            index += 1

        fraction_derivative_dict[name] = fraction_derivative

    return fraction_derivative_dict
