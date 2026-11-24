// validAlphabets
//
// Copied verbatim from https://github.com/Rickyslim/insects-detection-webui
//   file src/utils/validate.js, line 53
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Moths insects and insect traps
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function validAlphabets(str) {
  const reg = /^[A-Za-z]+$/
  return reg.test(str)
}
