// rotl
//
// Copied verbatim from https://github.com/WebOrigami/origami
//   file origami/src/origami/randomsFrom.js, line 31
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function rotl(x, k) {
  return ((x << k) | (x >>> (32 - k))) >>> 0;
}
