# fourier_derivative
#
# Copied verbatim from https://github.com/davofis/computational_seismology
#   notebook 05_pseudospectral/ps_derivative_solution.ipynb (its code cells joined in order; line 12 of those)
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def fourier_derivative(f, dx):
    # Length of vector f
    nx = np.size(f)
    # Initialize k vector up to Nyquist wavenumber      
    kmax = np.pi/dx
    dk = kmax/(nx/2)
    k = np.arange(float(nx))
    k[: int(nx/2)] = k[: int(nx/2)] * dk 
    k[int(nx/2) :] = k[: int(nx/2)] - kmax
    # Fourier derivative
    ff = np.fft.fft(f); ff = 1j*k*ff
    df_num = np.real(np.fft.ifft(ff))
    return df_num
