// groupByThree
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/graph/triangulate.js, line 46
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const groupByThree = (array) =>
	array.length === 3
		? [array]
		: Array.from(Array(Math.floor(array.length / 3))).map((_, i) =>
				[i * 3 + 0, i * 3 + 1, i * 3 + 2].map((j) => array[j]),
			);
