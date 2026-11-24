# apply_charge_balance
#
# Copied verbatim from https://github.com/islamshahine/geochemistry
#   file src/archive_cleanup/archive_old_engines/engine_refactored.py, line 986
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def apply_charge_balance(totals, balancing_cations=None, balancing_anions=None):
    """Apply charge balance to totals."""
    # Calculate current charge balance
    total_positive = 0.0
    total_negative = 0.0

    for species, concentration in totals.items():
        # Simple charge detection
        if species.endswith('+++'):
            total_positive += 3 * concentration
        elif species.endswith('++'):
            total_positive += 2 * concentration
        elif species.endswith('+'):
            total_positive += concentration
        elif species.endswith('---'):
            total_negative += 3 * concentration
        elif species.endswith('--'):
            total_negative += 2 * concentration
        elif species.endswith('-'):
            total_negative += concentration

    charge_imbalance = total_positive - total_negative

    # Apply charge balance if needed
    if abs(charge_imbalance) > 1e-12:
        if charge_imbalance > 0 and balancing_anions:
            # Need negative charge
            for anion in balancing_anions:
                if anion in totals:
                    totals[anion] += charge_imbalance
                    break
        elif charge_imbalance < 0 and balancing_cations:
            # Need positive charge
            for cation in balancing_cations:
                if cation in totals:
                    totals[cation] += abs(charge_imbalance)
                    break

    return totals
