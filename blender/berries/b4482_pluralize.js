// pluralize
//
// Copied verbatim from https://github.com/Rickyslim/insects-detection-webui
//   file src/filters/index.js, line 10
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Moths insects and insect traps
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function pluralize(time, label) {
  if (time === 1) {
    return time + label
  }
  return time + label + 's'
}
