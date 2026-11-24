// mapHexNumbers
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/svg/colors/convert.js, line 38
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
