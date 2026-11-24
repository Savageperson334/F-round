// resizeUp
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/math/vector.js, line 488
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const resize = (dimension, vector) =>
	vector.length === dimension
		? vector
		: Array(dimension)
				.fill(0)
				.map((z, i) => (vector[i] ? vector[i] : z));


const resizeUp = (a, b) =>
	[a, b].map((v) => resize(Math.max(a.length, b.length), v));
