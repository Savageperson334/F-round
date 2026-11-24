# unsupervised_binary_classification
#
# Copied verbatim from https://github.com/MinersAI/geochemical_anomaly_detection
#   file outlier_detection_functions.py, line 11
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def unsupervised_binary_classification(anomaly_scores, z_score: float = 3.5):  # Used to automatically classify the data points as inliers or outliers
    """
    Classifies data points as inliers or outliers using the Modified Z-Score method
    based on the Median Absolute Deviation (MAD).

    Outliers are identified as points with a modified Z-score greater than 3.5.

    Args:
        anomaly_scores (np.array): Computed anomaly scores
        z_score (float): Modified Z-score threshold for outlier classification (default: 3.5)

    Returns:
        np.array: Binary outlier classification (-1 outliers, 1 inliers)
    """
    median_score = np.median(anomaly_scores)
    mad = np.median(np.abs(anomaly_scores - median_score))
    modified_z_scores = 0.6745 * (anomaly_scores - median_score) / mad

    # Classify as outliers if modified z-score exceeds 3.5
    outlier_mask = np.abs(modified_z_scores) > z_score
    classifications = np.where(outlier_mask, -1, 1)

    return classifications
