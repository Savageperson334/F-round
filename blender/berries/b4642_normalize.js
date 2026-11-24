// normalize
//
// Copied verbatim from https://github.com/WebOrigami/origami
//   file language/src/runtime/typos.js, line 84
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function normalize(str) {
  return str.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
}
