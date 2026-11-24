// add2path
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/svg/general/path.js, line 36
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const add2path = (a, b) => [a[0] + (b[0] || 0), a[1] + (b[1] || 0)];
