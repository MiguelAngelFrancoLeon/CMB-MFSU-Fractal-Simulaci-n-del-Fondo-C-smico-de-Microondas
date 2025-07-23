
# Wavelet Analysis of CMB – MFSU Validation

This folder contains code and output for applying a wavelet transform to a temperature profile of the Cosmic Microwave Background (CMB) using the SMICA map from Planck DR3.

## Files

- `fractal_analysis.py`: Python script performing the analysis.
- `wavelet_fractal_plot.png`: Log-log plot of wavelet power vs scale.
- `result.txt`: Estimated fractal dimension (Df) based on the slope.

## Interpretation

The estimated slope allows us to compute the fractal dimension Df using:

    Df = (5 + slope) / 2

This supports the MFSU model if Df ≈ 0.92.
