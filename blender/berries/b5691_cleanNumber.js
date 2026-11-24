// cleanNumber
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/general/number.js, line 24
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const countPlaces = function (num) {
	const m = `${num}`.match(/(?:\.(\d+))?(?:[eE]([+-]?\d+))?$/);
	return Math.max(0, (m[1] ? m[1].length : 0) - (m[2] ? +m[2] : 0));
};


const cleanNumber = function (number, places = 15) {
	const num = typeof number === "number" ? number : parseFloat(number);
	if (Number.isNaN(num)) {
		return number;
	}
	const crop = parseFloat(num.toFixed(places));
	if (countPlaces(crop) === Math.min(places, countPlaces(num))) {
		return num;
	}
	return crop;
};
