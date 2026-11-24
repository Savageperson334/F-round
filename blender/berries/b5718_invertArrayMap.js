// invertArrayMap
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/graph/maps.js, line 63
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const invertArrayMap = (map) => {
	const inv = [];
	map.forEach((arr, i) =>
		arr.forEach((m) => {
			if (inv[m] === undefined) {
				inv[m] = [];
			}
			inv[m].push(i);
		}),
	);
	return inv;
};
