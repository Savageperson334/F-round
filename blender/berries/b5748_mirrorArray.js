// mirrorArray
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/math/convexHull.js, line 15
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const mirrorArray = (arr) => arr.concat(arr.slice(0, -1).reverse());
