// genericRateUnitLabel
//
// Copied verbatim from https://github.com/NCAR/music-box-interactive
//   file src/utils/rateParameterUnits.js, line 74
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Mechanical music boxes and organs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const GAP = ' \u2009'


function genericRateUnitLabel(unitId, offset) {
  // The exponent is n - 1 + offset.
  const exponent = offset === 1 ? 'n' : `(n-${1 - offset})`
  return unitId === 'molecule'
    ? `(cm^3${GAP}molecule^-1)^${exponent}${GAP}s^-1`
    : `(mol${GAP}m^-3)^-${exponent}${GAP}s^-1`
}
