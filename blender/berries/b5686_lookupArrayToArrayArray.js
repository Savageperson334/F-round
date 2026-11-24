// lookupArrayToArrayArray
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/general/array.js, line 337
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const lookupArrayToArrayArray = (lookupArray) =>
	lookupArray.map((array) =>
		array.map((overlap, i) => (overlap ? i : undefined)).filter((a) => a !== undefined),
	);
