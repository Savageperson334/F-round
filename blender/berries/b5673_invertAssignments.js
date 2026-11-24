// invertAssignments
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/fold/spec.js, line 527
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const flipAssignmentLookup = { M: "V", m: "v", V: "M", v: "m" };


const invertAssignments = (graph) => {
	if (graph.edges_assignment) {
		graph.edges_assignment = graph.edges_assignment.map((a) =>
			flipAssignmentLookup[a] ? flipAssignmentLookup[a] : a,
		);
	}
	if (graph.edges_foldAngle) {
		graph.edges_foldAngle = graph.edges_foldAngle.map((n) => -n);
	}
	return graph;
};
