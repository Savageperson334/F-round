// boundingBox
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/math/polygon.js, line 185
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const getDimension = (points) => {
	for (let i = 0; i < points.length; i += 1) {
		if (points[i] && points[i].length) {
			return points[i].length;
		}
	}
	return 0;
};


const boundingBox = (points, padding = 0) => {
	if (!points || !points.length) {
		return undefined;
	}
	const dimension = getDimension(points);
	const min = Array(dimension).fill(Infinity);
	const max = Array(dimension).fill(-Infinity);
	points
		.filter((p) => p !== undefined)
		.forEach((point) =>
			point.forEach((c, i) => {
				if (c < min[i]) {
					min[i] = c;
				}
				if (c > max[i]) {
					max[i] = c;
				}
			}),
		);
	for (let i = 0; i < dimension; i += 1) {
		min[i] -= padding;
		max[i] += padding;
	}
	const span = max.map((m, i) => m - min[i]);
	return { min, max, span };
};
