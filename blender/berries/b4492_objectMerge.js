// objectMerge
//
// Copied verbatim from https://github.com/Rickyslim/insects-detection-webui
//   file src/utils/index.js, line 198
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Moths insects and insect traps
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function objectMerge(target, source) {
  if (typeof target !== 'object') {
    target = {}
  }
  if (Array.isArray(source)) {
    return source.slice()
  }
  Object.keys(source).forEach(property => {
    const sourceProperty = source[property]
    if (typeof sourceProperty === 'object') {
      target[property] = objectMerge(target[property], sourceProperty)
    } else {
      target[property] = sourceProperty
    }
  })
  return target
}
