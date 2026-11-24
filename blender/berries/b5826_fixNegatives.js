// fixNegatives
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/svg/constructor/extensions/rect.js, line 25
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const fixNegatives = function (arr) {
	[0, 1].forEach((i) => {
		if (arr[2 + i] < 0) {
			if (arr[0 + i] === undefined) {
				arr[0 + i] = 0;
			}
			arr[0 + i] += arr[2 + i];
			arr[2 + i] = -arr[2 + i];
		}
	});
	return arr;
};
