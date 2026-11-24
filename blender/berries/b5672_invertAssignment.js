// invertAssignment
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/fold/spec.js, line 519
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const flipAssignmentLookup = { M: "V", m: "v", V: "M", v: "m" };


const invertAssignment = (assign) => flipAssignmentLookup[assign] || assign;
