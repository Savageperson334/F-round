// reactionWithSpeciesNames
//
// Copied verbatim from https://github.com/NCAR/music-box-interactive
//   file src/services/mechanism/speciesIds.js, line 104
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Mechanical music boxes and organs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const COMPONENT_KEYS = [
  'reactants',
  'products',
  'gas-phase products',
  'alkoxy products',
  'nitrate products',
]

const SURFACE_SPECIES_ID_KEY = 'gas-phase species id'

const SURFACE_SPECIES_KEY = 'gas-phase species'


const isObject = (value) => value !== null && typeof value === 'object'


function componentToName(component, names) {
  if (!isObject(component) || !component.speciesId) return component
  const { speciesId, ...rest } = component
  return { name: names.get(speciesId), ...rest }
}


function reactionWithSpeciesNames(reaction, names) {
  if (!isObject(reaction)) return reaction
  const next = { ...reaction }
  COMPONENT_KEYS.forEach((key) => {
    if (Array.isArray(next[key])) next[key] = next[key].map((c) => componentToName(c, names))
  })
  if (SURFACE_SPECIES_ID_KEY in next) {
    next[SURFACE_SPECIES_KEY] = names.get(next[SURFACE_SPECIES_ID_KEY])
    delete next[SURFACE_SPECIES_ID_KEY]
  }
  return next
}
