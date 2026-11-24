// parseVertex
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/convert/objToFold.js, line 81
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const parseVertex = (vertex) => {
	const [a, b, c] = vertex.slice(1).map((str) => parseFloat(str));
	return [a || 0, b || 0, c || 0];
};
