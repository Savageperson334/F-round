# output_image_filename
#
# Copied verbatim from https://github.com/zhoubolei/cnnvisualizer
#   file tightcrop.py, line 146
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def output_image_filename(basename, iter, zunit):
#    return ('/data/vision/torralba/gigaSUN/www/unit_annotation/result_segments_iterations' +
    return ('/data/vision/torralba/scratch2/davidbau/iccv' +
        '/%s_iter_%d/html/image/conv5-%04d_crop.jpg' % (basename, iter, zunit))
