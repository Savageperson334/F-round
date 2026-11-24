// hexToRgb
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/svg/colors/convert.js, line 54
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const mapHexNumbers = (numbers, map) => {
	// ensure a minimum number of characters (fill 0 if needed)
	const chars = Array.from(Array(map.length)).map((_, i) => numbers[i] || "0");
	// handle abbreviated hex codes: #fb4 or #fb48 (with alpha)
	return numbers.length <= 4 ? map.map((i) => chars[i]).join("") : chars.join("");
};


const roundF = (n) => Math.round(n * 100) / 100;


const hexToRgb = (string) => {
	const numbers = string.replace(/#(?=\S)/g, "");
	const hasAlpha = numbers.length === 4 || numbers.length === 8;
	const hexString = hasAlpha
		? mapHexNumbers(numbers, [0, 0, 1, 1, 2, 2, 3, 3])
		: mapHexNumbers(numbers, [0, 0, 1, 1, 2, 2]);
	const c = parseInt(hexString, 16);
	return hasAlpha
		? [(c >> 24) & 255, (c >> 16) & 255, (c >> 8) & 255, roundF((c & 255) / 255)]
		: [(c >> 16) & 255, (c >> 8) & 255, c & 255];
};
