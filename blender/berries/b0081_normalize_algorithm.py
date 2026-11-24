# normalize_algorithm
#
# Copied verbatim from https://github.com/Augtumn/IsoLeadToolkit
#   file visualization/plotting/rendering/embedding/algorithm.py, line 36
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def _resolve_mode_aliases(value: str) -> str | None:
    """Map alternate render-mode/algorithm names to their canonical form.

    The isochron overlay code emits ISOCHRON1/ISOCHRON2 (and group selection
    produces PB_MODELS_*), so both spellings reach normalize_algorithm and the
    legend's ``normalize_render_mode``; the mapping lives here once. Returns
    ``None`` when *value* needs no mapping (callers apply their own case
    convention).

    Note: *value* must already be normalized to the caller's case
    convention (upper for algorithms, verbatim for legend render modes).
    """
    if value in ('PB_MODELS_76', 'PB_MODELS_86'):
        return 'PB_EVOL_76' if value.endswith('_76') else 'PB_EVOL_86'
    if value in ('ISOCHRON1', 'ISOCHRON2'):
        return 'PB_EVOL_76' if value == 'ISOCHRON1' else 'PB_EVOL_86'
    return None


def normalize_algorithm(algorithm: str) -> str:
    """Normalize alternate algorithm names to canonical names."""
    actual_algorithm = algorithm.strip().upper() if isinstance(algorithm, str) else str(algorithm)
    if actual_algorithm == 'ROBUSTPCA':
        return 'RobustPCA'
    canonical = _resolve_mode_aliases(actual_algorithm)
    if canonical is not None:
        return canonical
    return actual_algorithm
