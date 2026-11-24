# format_2vectors
#
# Copied verbatim from https://github.com/holodyne/slmsuite
#   file slmsuite/holography/toolbox/__init__.py, line 1069
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Optical computing and holograms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def format_vectors(vectors, expected_dimension=2, handle_dimension="pass"):
    """
    Validates that an array of M-dimensional vectors is a ``numpy.ndarray`` of shape ``(M, N)``.
    Handles shaping and transposing if, for instance, tuples or row vectors are passed.

    Parameters
    ----------
    vectors : array_like
        M-vector or array of M-vectors to process. Desires shape of ``(M, N)``.
    expected_dimension : int
        Dimension of the system, i.e. ``M``.
    handle_dimension : {"error", "crop", "pass"}
        If an array of vectors with larger dimensionality than
        ``expected_dimension = M`` is provided, decides how to handle these:

        - ``"error"`` Raises an error if not ``(M, N)``.

        - ``"crop"`` Crops the higher dimensions and returns ``(M, N)``.

        - ``"pass"`` Returns ``(K, N)`` if ``K`` is greater than or equal to ``M``.

        If the array has smaller dimensionality than expected, an error is always raised.

    Returns
    -------
    vectors : numpy.ndarray
        Cleaned column vector(s). Shape of ``(M, N)``.

    Raises
    ------
    ValueError
        If the vector input was inappropriate.
    """
    # Parse expected_dimension
    expected_dimension = int(expected_dimension)

    # Parse handle_dimension
    options_dimension = ["error", "crop", "pass"]
    if handle_dimension not in options_dimension:
        raise ValueError(
            f"handle_dimension option '{handle_dimension}' not recognized. "
            f"Must be one of '{options_dimension}'."
        )

    # Convert to np.array and squeeze
    vectors = np.squeeze(vectors)

    # Handle the singleton cases.
    if len(vectors.shape) == 1:
        vectors = vectors[:, np.newaxis]
    elif len(vectors.shape) == 2 and vectors.shape[0] == 1:
        vectors = vectors.T

    # Make sure that we are an array of N M-vectors.
    if len(vectors.shape) != 2:
        raise ValueError(f"Wrong dimension {vectors.shape} for vectors.")

    if vectors.shape[0] == expected_dimension:
        pass
    elif vectors.shape[0] > expected_dimension:  # Handle unexpected case.
        if handle_dimension == "pass":
            pass
        elif handle_dimension == "crop":
            if vectors.shape[0] > expected_dimension:
                vectors = vectors[:expected_dimension, :]
            else:
                raise ValueError(
                    f"{vectors.shape[0]}-vectors too small to crop to {expected_dimension}-vectors."
                )
        elif handle_dimension == "error":
            raise ValueError(
                f"Expected {expected_dimension}-vectors. Found {vectors.shape[0]}-vectors."
            )
    else:
        raise ValueError(
            f"Expected {expected_dimension}-vectors. Found {vectors.shape[0]}-vectors."
        )

    return vectors


def format_2vectors(vectors):
    """
    Validates that an array of 2-dimensional vectors is a ``numpy.ndarray`` of shape ``(2, N)``.
    Handles shaping and transposing if, for instance, tuples or row vectors are passed.
    This is a wrapper of :meth:`format_vectors` for backwards compatibility.

    Parameters
    ----------
    vectors : array_like
        2-vector or array of 2-vectors to process. Desires shape of ``(2, N)``.
        Uses the ``"crop"`` keyword of :meth:`format_vectors`.

    Returns
    -------
    vectors : numpy.ndarray
        Cleaned column vector(s). Shape of ``(2, N)``.

    Raises
    ------
    ValueError
        If the vector input was inappropriate.
    """
    return format_vectors(vectors, expected_dimension=2, handle_dimension="crop")
