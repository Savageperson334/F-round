// distance
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/math/vector.js, line 329
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const safeAdd = (a, b) => a + (b || 0);


const distance = (v, u) =>
	Math.sqrt(v.map((_, i) => (v[i] - u[i]) ** 2).reduce(safeAdd, 0));
