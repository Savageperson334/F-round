// findValue
//
// Copied verbatim from https://github.com/willianantunes/rave-of-phonetics
//   file frontend/src/config/settings.js, line 20
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Languages scripts and morphology
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function findValue(v1, v2) {
  return [v1, v2].filter(v => v)[0]
}
