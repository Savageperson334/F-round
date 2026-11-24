// svg_polar_to_cart
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/svg/general/algebra.js, line 28
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const svg_polar_to_cart = (a, d) => [Math.cos(a) * d, Math.sin(a) * d];
