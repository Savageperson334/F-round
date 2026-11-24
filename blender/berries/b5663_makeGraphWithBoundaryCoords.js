// makeGraphWithBoundaryCoords
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/fold/primitives.js, line 29
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const makeGraphWithBoundaryCoords = (vertices_coords) => ({
	vertices_coords,
	edges_vertices: vertices_coords.map((_, i, arr) => [i, (i + 1) % arr.length]),
	edges_assignment: Array(vertices_coords.length).fill("B"),
	faces_vertices: [vertices_coords.map((_, i) => i)],
	faces_edges: [vertices_coords.map((_, i) => i)],
});
