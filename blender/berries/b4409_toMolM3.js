// toMolM3
//
// Copied verbatim from https://github.com/NCAR/music-box-interactive
//   file src/utils/concentrationUnits.js, line 49
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Mechanical music boxes and organs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const MIXING_RATIO_FACTORS = {
  mol_mol: 1,
  ppth: 1e-3,
  ppm: 1e-6,
  ppb: 1e-9,
  ppt: 1e-12,
}

const AVOGADRO_CONSTANT = 6.02214076e23

const NUMBER_DENSITY_FACTORS = {
  molecule_cm3: AVOGADRO_CONSTANT * 1e-6,
}


function isMixingRatioUnit(unitId) {
  return unitId in MIXING_RATIO_FACTORS
}


function isNumberDensityUnit(unitId) {
  return unitId in NUMBER_DENSITY_FACTORS
}


function concentrationDivisor(unitId, airDensity) {
  if (isMixingRatioUnit(unitId)) return MIXING_RATIO_FACTORS[unitId] * airDensity
  if (isNumberDensityUnit(unitId)) return 1 / NUMBER_DENSITY_FACTORS[unitId]
  return 1
}


function toMolM3(value, unitId, airDensity) {
  return value * concentrationDivisor(unitId, airDensity)
}
