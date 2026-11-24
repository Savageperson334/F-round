# apply_charge_balance
#
# Copied verbatim from https://github.com/islamshahine/geochemistry
#   file src/archive_cleanup/archive_old_engines/engine_backup.py, line 754
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def apply_charge_balance(totals, balancing_cations=None, balancing_anions=None):
    """Apply charge balance to input concentrations."""
    if balancing_cations is None:
        balancing_cations = ['Na+', 'K+']
    if balancing_anions is None:
        balancing_anions = ['Cl-']

    # Calculate current charge balance
    total_positive = 0.0
    total_negative = 0.0

    for species_name, concentration in totals.items():
        # Get charge from species database
        charge = 0
        if species_name in ['Na+', 'K+', 'Ca++', 'Mg++', 'NH4+', 'Fe++', 'Fe+++', 'Al+++']:
            charge = 1 if '+' in species_name else 2 if '++' in species_name else 3
        elif species_name in ['Cl-', 'Br-', 'NO3-', 'NO2-', 'HCO3-', 'F-', 'CN-']:
            charge = -1
        elif species_name in ['SO4--', 'CO3--', 'HPO4--', 'S--']:
            charge = -2
        elif species_name in ['PO4---']:
            charge = -3

        if charge > 0:
            total_positive += charge * concentration
        elif charge < 0:
            total_negative += abs(charge) * concentration

    # Calculate charge imbalance
    charge_imbalance = total_positive - total_negative

    # Apply charge balance
    balanced_totals = totals.copy()

    if charge_imbalance > 0:  # Excess positive charge
        # Add balancing anion
        for anion in balancing_anions:
            if anion not in balanced_totals:
                balanced_totals[anion] = charge_imbalance
                break
    elif charge_imbalance < 0:  # Excess negative charge
        # Add balancing cation
        for cation in balancing_cations:
            if cation not in balanced_totals:
                balanced_totals[cation] = abs(charge_imbalance)
                break

    return balanced_totals
