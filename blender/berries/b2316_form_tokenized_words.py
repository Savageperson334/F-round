# form_tokenized_words
#
# Copied verbatim from https://github.com/isi-vista/VistaOCR
#   file src/textutils.py, line 290
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def form_tokenized_words(chars, with_spaces=False):
    punctuations = {"u002e", "u002c", "u003b", "u0027", "u0022", "u002f", "u0021", "u0028", "u0029", "u005b", "u005d", "u003c", "u003e",
                   "u002d", "u005f", "u007b", "u007d", "u0024", "u0025", "u0023", "u0026", "u060c", "u201d", "u060d", "u060f", "u061f",
                   "u066d", "ufd3e", "ufd3f", "u061e", "u066a", "u066b", "u066c", "u002a", "u002b", "u003a", "u003d", "u005e", "u0060", "u007c", "u007e"}
    digits = {
        "u0660", "u0661", "u0662", "u0663", "u0664", "u0665", "u0666", "u0667", "u0668", "u0669", "u0030", "u0031",
        "u0032", "u0033", "u0034", "u0035", "u0036", "u0037", "u0038", "u0039"
    }

    words = []
    start_idx = 0
    for i in range(len(chars)):
        if chars[i] == 'u0020':  # Space denotes new word
            if start_idx != i:
                words.append('_'.join(chars[start_idx:i]))

                if with_spaces:
                    words.append("u0020")
            start_idx = i + 1
            continue
        if chars[i] in punctuations or chars[i] in digits:
            if start_idx != i:
                words.append('_'.join(chars[start_idx:i]))
            words.append(chars[i])
            start_idx = i + 1
            continue
        if i == len(chars) - 1:
            # At end of line, so just toss remaining line into word array
            if start_idx == i:
                words.append(chars[start_idx])
            else:
                words.append('_'.join(chars[start_idx:]))

    return words
