// normalize2
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/math/vector.js, line 76
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const magnitude2 = (v) => Math.sqrt(v[0] * v[0] + v[1] * v[1]);


const normalize2 = (v) => {
	const m = magnitude2(v);
	return m === 0 ? [v[0], v[1]] : [v[0] / m, v[1] / m];
};
