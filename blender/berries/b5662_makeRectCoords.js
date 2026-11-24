// makeRectCoords
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/fold/primitives.js, line 14
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const makeRectCoords = (w, h) => [
	[0, 0],
	[w, 0],
	[w, h],
	[0, h],
];
