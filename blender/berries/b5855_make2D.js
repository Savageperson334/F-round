// make2D
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/webgl/creasePattern/data.js, line 11
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const make2D = (coords) => coords.map(([x, y]) => [x || 0, y || 0]);
