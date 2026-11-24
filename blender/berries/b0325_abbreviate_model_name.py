# abbreviate_model_name
#
# Copied verbatim from https://github.com/IGeochemCloud/Hg-MC-Auto
#   file src/5.Exter_ML_train.py, line 288
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def abbreviate_model_name(full_name):
    """Abbreviate model names including sampling method for plotting"""
    # Split by underscore to separate model and sampling method
    parts = full_name.split('_')
    model_part = parts[0]
    sampling_part = '_'.join(parts[1:]) if len(parts) > 1 else 'Orig'

    # Model name mapping
    name_mapping = {
        'Logistic Regression': 'LR',
        'Random Forest': 'RF',
        'Support Vector Machine': 'SVM',
        'SVM': 'SVM',
        'K-Nearest Neighbors': 'KNN',
        'KNN': 'KNN',
        'Decision Tree': 'DT',
        'Gradient Boosting': 'GB',
        'Naive Bayes': 'NB',
        'XGBoost': 'XGB',
        'Bagging RF': 'BagRF'
    }

    # Sampling method abbreviation
    sampling_mapping = {
        'SMOTE': 'S',
        'ADASYN': 'A',
        'SMOTEENN': 'SE',
        'UnderSampling': 'U',
        'Original': 'Orig',
        'Orig': 'Orig'
    }

    # Get abbreviations
    model_abbr = name_mapping.get(model_part, model_part[:6])
    sampling_abbr = sampling_mapping.get(sampling_part, sampling_part[:3])

    # Combine with underscore
    if sampling_abbr == 'Orig':
        return f"{model_abbr}"
    else:
        return f"{model_abbr}_{sampling_abbr}"
