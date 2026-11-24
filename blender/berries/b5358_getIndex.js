// getIndex
//
// Copied verbatim from https://github.com/magicshifter/ms4000
//   file web/app/src/reducers/pixelEditor.js, line 47
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function getIndex(state, x, y) {
  return state.width * y + x
}
