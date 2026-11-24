// makeTriangleFan
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/graph/triangulate.js, line 20
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const makeTriangleFan = (indices) =>
	Array.from(Array(indices.length - 2)).map((_, i) => [
		indices[0],
		indices[i + 1],
		indices[i + 2],
	]);
