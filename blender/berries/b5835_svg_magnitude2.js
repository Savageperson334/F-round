// svg_magnitude2
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/svg/general/algebra.js, line 19
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const svg_magnitudeSq2 = (a) => a[0] ** 2 + a[1] ** 2;


const svg_magnitude2 = (a) => Math.sqrt(svg_magnitudeSq2(a));
