// makePerspectiveMatrix4
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/math/matrix4.js, line 317
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const makePerspectiveMatrix4 = (FOV, aspect, near, far) => {
	const f = Math.tan(Math.PI * 0.5 - 0.5 * FOV);
	const rangeInv = 1.0 / (near - far);
	const x = aspect < 1 ? f : f / aspect;
	const y = aspect < 1 ? f * aspect : f;
	return [
		x,
		0,
		0,
		0,
		0,
		y,
		0,
		0,
		0,
		0,
		(near + far) * rangeInv,
		-1,
		0,
		0,
		near * far * rangeInv * 2,
		0,
	];
};
