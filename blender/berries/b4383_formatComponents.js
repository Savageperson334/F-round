// formatComponents
//
// Copied verbatim from https://github.com/NCAR/music-box-interactive
//   file src/services/results/downloadResults.js, line 9
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Mechanical music boxes and organs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function formatComponents(components) {
  if (!Array.isArray(components) || components.length === 0) {
    return '∅'
  }
  return components
    .map((component) => {
      const name = component?.name || ''
      const coefficient = Number(component?.coefficient)
      const prefix = Number.isFinite(coefficient) && coefficient !== 1 ? `${coefficient} ` : ''
      return `${prefix}${name}`
    })
    .join(' + ')
}
