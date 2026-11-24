// makeVertexFans
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/graph/boundary/cut.js, line 30
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const makeVertexFans = (vertex_edgesIsCut, vertex_faces) => {
	const n = vertex_edgesIsCut.length;

	// does wedge j continue the fan of the wedge before it (across edge j)?
	// this requires that both wedges have a face, and the edge is not a cut.
	const wedges_joined = vertex_faces.map(
		(face, j) =>
			vertex_faces[(j + n - 1) % n] != null && face != null && !vertex_edgesIsCut[j],
	);

	// a wedge that is not joined to its predecessor starts a new fan. walk
	// around the vertex, labelling each wedge with the most recent start.
	// wedges before the first start belong to the last start (wrap around).
	const startCount = wedges_joined.filter((joined) => !joined).length;
	let label = startCount - 1;
	let startsSeen = 0;
	const wedges_label = wedges_joined.map((joined) => {
		if (!joined) {
			label = startsSeen;
			startsSeen += 1;
		}
		return label;
	});

	// wedges without a face don't get a fan (no vertex without faces).
	// renumber so fans are 0...k, in order of appearance. fan 0 keeps the vertex.
	const labelFan = {};
	let fanCount = 0;
	wedges_label.forEach((wedgeLabel, j) => {
		if (vertex_faces[j] == null || labelFan[wedgeLabel] !== undefined) {
			return;
		}
		labelFan[wedgeLabel] = fanCount;
		fanCount += 1;
	});
	const wedges_fan = wedges_label.map((wedgeLabel, j) =>
		vertex_faces[j] == null ? undefined : labelFan[wedgeLabel],
	);

	// edge j sits between wedge j-1 (clockwise) and wedge j (counter-clockwise).
	// if only one side has a face, both sides use that face's fan.
	/** @type {[number, number][]} */
	const edges_fans = vertex_edgesIsCut.map((_, j) => {
		const clockwise = wedges_fan[(j + n - 1) % n];
		const counterClockwise = wedges_fan[j];
		if (clockwise === undefined && counterClockwise === undefined) {
			return [0, 0];
		}
		if (clockwise === undefined) {
			return [counterClockwise, counterClockwise];
		}
		if (counterClockwise === undefined) {
			return [clockwise, clockwise];
		}
		return [clockwise, counterClockwise];
	});

	return {
		count: Math.max(fanCount, 1),
		wedges_fan,
		edges_fans,
	};
};
