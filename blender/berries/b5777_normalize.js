// normalize
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/math/vector.js, line 66
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const safeAdd = (a, b) => a + (b || 0);


const magnitude = (v) => Math.sqrt(v.map((n) => n * n).reduce(safeAdd, 0));


const normalize = (v) => {
	const m = magnitude(v);
	return m === 0 ? v.slice() : v.map((c) => c / m);
};
