# ds2_mean_uint16
#
# Copied verbatim from https://github.com/mesoSPIM/mesoSPIM-control
#   file mesoSPIM/src/plugins/support_files/ImageWriters/OmeZarrWriter/omezarr_writer.py, line 31
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Microscopy & small worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def ds2_mean_uint16(img: np.ndarray) -> np.ndarray:
    y, x = img.shape
    y2 = y - (y & 1); x2 = x - (x & 1)
    out = img[:y2:2, :x2:2].astype(np.uint32)
    out += img[1:y2:2, :x2:2].astype(np.uint32)
    out += img[:y2:2, 1:x2:2].astype(np.uint32)
    out += img[1:y2:2, 1:x2:2].astype(np.uint32)
    out += 2 # +2 to mean round divide by 4
    out[:] = out >> 2
    # pad edge by replication if odd dims:
    if y & 1: out = np.vstack([out, out[-1:]])
    if x & 1: out = np.hstack([out, out[:, -1:]])
    return out.astype(np.uint16)
