// get_opposite_assignment
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/graph/fold/flatFold.js, line 590
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const opposite_lookup = {
	M: "V",
	m: "V",
	V: "M",
	v: "M",
};


const get_opposite_assignment = (assign) => opposite_lookup[assign] || assign;
