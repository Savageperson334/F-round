# cut_to_chunks
#
# Copied verbatim from https://github.com/Phoenix-64/APT-Telemetry-Decoder
#   file research.py, line 52
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sensors and telemetry
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def cut_to_chunks(data, start, l):
    first_index = start - (start // l * l)
    last_index = start + ((len(data) - start) // l * l) - l
    nr_blocks = (last_index - first_index) // l

    return first_index, nr_blocks
