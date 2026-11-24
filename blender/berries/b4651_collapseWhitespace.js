// collapseWhitespace
//
// Copied verbatim from https://github.com/WebOrigami/origami
//   file origami/src/origami/domObject.js, line 96
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function collapseWhitespace(str) {
  return str.replace(/^\s+/, " ").replace(/\s+$/, " ");
}
