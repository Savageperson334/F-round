# generate_locations
#
# Copied verbatim from https://github.com/misaelmalqui/Electron-beam-for-crystal-structres-simulation
#   file Code/Animations_preamble.py, line 183
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Molecular shapes and crystal lattices
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def generate_locations(Z):
    d1s = ['-d1', '-d2', '-d3', '-d4', '-d5', '-d6', '-d7', '-d8', '-d9']
    d2s = ['-00', '-50']
    locations = []

    for d1 in d1s:
        for d2 in d2s:
            locations.append('Z' + str(Z) + '/results' + d1 + d2 + '.txt')
    locations.append('Z' + str(Z) + '/results-d10-00.txt')

    return locations
