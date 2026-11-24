// rateUnitLabel
//
// Copied verbatim from https://github.com/NCAR/music-box-interactive
//   file src/utils/rateParameterUnits.js, line 61
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Mechanical music boxes and organs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const GAP = ' \u2009'


function rateUnitLabel(unitId, order) {
  const power = order - 1
  if (power === 0) return 's^-1'
  const volume = unitId === 'molecule' ? 'cm' : 'm'
  const amount = unitId === 'molecule' ? 'molecule' : 'mol'
  if (power < 0) {
    const amountPower = power === -1 ? '' : `^${-power}`
    return `${amount}${amountPower}${GAP}${volume}^${3 * power}${GAP}s^-1`
  }
  return `${volume}^${3 * power}${GAP}${amount}^-${power}${GAP}s^-1`
}
