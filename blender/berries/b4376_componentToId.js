// componentToId
//
// Copied verbatim from https://github.com/NCAR/music-box-interactive
//   file src/services/mechanism/speciesIds.js, line 41
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Mechanical music boxes and organs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const isObject = (value) => value !== null && typeof value === 'object'


function componentToId(component, ids) {
  if (!isObject(component) || component.speciesId || !ids.has(component.name)) return component
  const { name, ...rest } = component
  return { speciesId: ids.get(name), ...rest }
}
