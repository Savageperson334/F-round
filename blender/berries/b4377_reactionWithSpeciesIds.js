// reactionWithSpeciesIds
//
// Copied verbatim from https://github.com/NCAR/music-box-interactive
//   file src/services/mechanism/speciesIds.js, line 48
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

const SURFACE_SPECIES_KEY = 'gas-phase species'

const SURFACE_SPECIES_ID_KEY = 'gas-phase species id'


const isObject = (value) => value !== null && typeof value === 'object'


const idsByName = (species = []) => new Map(species.filter((s) => s?.id).map((s) => [s.name, s.id]))


function componentToId(component, ids) {
  if (!isObject(component) || component.speciesId || !ids.has(component.name)) return component
  const { name, ...rest } = component
  return { speciesId: ids.get(name), ...rest }
}


function reactionWithSpeciesIds(reaction, species) {
  if (!isObject(reaction)) return reaction
  const ids = idsByName(species)
  const next = { ...reaction }
  COMPONENT_KEYS.forEach((key) => {
    if (Array.isArray(next[key])) next[key] = next[key].map((c) => componentToId(c, ids))
  })
  const surfaceSpecies = next[SURFACE_SPECIES_KEY]
  if (typeof surfaceSpecies === 'string' && ids.has(surfaceSpecies)) {
    delete next[SURFACE_SPECIES_KEY]
    next[SURFACE_SPECIES_ID_KEY] = ids.get(surfaceSpecies)
  }
  return next
}
