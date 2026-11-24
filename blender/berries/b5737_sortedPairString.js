// sortedPairString
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/layer/general.js, line 70
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const sortedPairString = (pair) =>
	pair[0] < pair[1] ? `${pair[0]} ${pair[1]}` : `${pair[1]} ${pair[0]}`;
