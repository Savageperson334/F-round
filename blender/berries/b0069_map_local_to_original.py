# map_local_to_original
#
# Copied verbatim from https://github.com/Augtumn/IsoLeadToolkit
#   file plugins/builtins/neighborhood_plugin.py, line 12
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def map_local_to_original(local_index: int, orig_indices: np.ndarray | None) -> int:
    """Map a subset-local index back to the original dataframe position.

    When a subset is active, embeddings are sliced with ``embedding[idx_list]``
    so positions inside the slice are local. This helper resolves a local
    position back to the original dataframe row index.

    Args:
        local_index: position inside the sliced (subset) array
        orig_indices: the ``idx_list`` used to slice, or None when no subset

    Returns:
        The original dataframe position; ``local_index`` itself when
        ``orig_indices`` is None or ``local_index`` is out of range.
    """
    if orig_indices is not None and 0 <= local_index < len(orig_indices):
        return int(orig_indices[local_index])
    return int(local_index)
