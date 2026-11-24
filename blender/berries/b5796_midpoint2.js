// midpoint2
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/math/vector.js, line 231
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const scale2 = (v, s) => [v[0] * s, v[1] * s];


const add2 = (v, u) => [v[0] + u[0], v[1] + u[1]];


const midpoint2 = (v, u) => scale2(add2(v, u), 0.5);
