// isInteger
//
// Copied verbatim from https://github.com/magicshifter/ms4000
//   file web/app/src/utils/types.js, line 9
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function  isInteger(n) {
  return n === +n && n === (n | 0)
}
