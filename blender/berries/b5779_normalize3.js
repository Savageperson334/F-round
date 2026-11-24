// normalize3
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/math/vector.js, line 86
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const magnitude3 = (v) => Math.sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2]);


const normalize3 = (v) => {
	const m = magnitude3(v);
	return m === 0 ? [v[0], v[1], v[2]] : [v[0] / m, v[1] / m, v[2] / m];
};
