# generate_destinations
#
# Copied verbatim from https://github.com/misaelmalqui/Electron-beam-for-crystal-structres-simulation
#   file Code/Animations_preamble.py, line 195
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Molecular shapes and crystal lattices
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def generate_destinations(Z):
    d1s = ['-d1', '-d2', '-d3', '-d4', '-d5', '-d6', '-d7', '-d8', '-d9']
    d2s = ['-00', '-50']
    destinations = []

    for d1 in d1s:
        for d2 in d2s:
            destinations.append('Z' + str(Z) + '/diffraction' + d1 + d2 + '.png')
    destinations.append('Z' + str(Z) + '/diffraction-d10-00.png')

    return destinations
