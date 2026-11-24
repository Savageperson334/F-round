# split_images_labels
#
# Copied verbatim from https://github.com/SubhrajyotiSen/KannadaHandwritingRecognition
#   file CNN/load_images.py, line 28
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def split_images_labels(images_labels):
    images = []
    labels = []
    for (image, label) in images_labels:
        images.append(image)
        labels.append(label)
    return images, labels
