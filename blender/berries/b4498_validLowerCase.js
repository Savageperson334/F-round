// validLowerCase
//
// Copied verbatim from https://github.com/Rickyslim/insects-detection-webui
//   file src/utils/validate.js, line 35
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Moths insects and insect traps
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function validLowerCase(str) {
  const reg = /^[a-z]+$/
  return reg.test(str)
}
