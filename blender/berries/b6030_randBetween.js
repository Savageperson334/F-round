// randBetween
//
// Copied verbatim from https://github.com/syfxlin/origami
//   file js/mouse.js, line 78
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function randBetween(min, max) {
  return Math.floor(Math.random() * max) + min;
}
