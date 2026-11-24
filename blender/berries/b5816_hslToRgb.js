// hslToRgb
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/svg/colors/convert.js, line 22
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const hslToRgb = (hue, saturation, lightness, alpha) => {
	const s = saturation / 100;
	const l = lightness / 100;
	/** @param {number} n */
	const k = (n) => (n + hue / 30) % 12;
	const a = s * Math.min(l, 1 - l);
	/** @param {number} n */
	const f = (n) => l - a * Math.max(-1, Math.min(k(n) - 3, Math.min(9 - k(n), 1)));
	return alpha === undefined
		? [f(0) * 255, f(8) * 255, f(4) * 255]
		: [f(0) * 255, f(8) * 255, f(4) * 255, alpha];
};
