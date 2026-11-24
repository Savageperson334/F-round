// downsample
//
// Copied verbatim from https://github.com/xcontcom/neuroparticles2
//   file legacy/particles.js, line 361
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Artificial life
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function downsample(array) {
	let size = array.length / 2;
	let result = [];

	for (let x = 0; x < size; x++) {
		result[x] = [];
		for (let y = 0; y < size; y++) {
			let v0 = array[x * 2][y * 2];
			let v1 = array[x * 2 + 1][y * 2];
			let v2 = array[x * 2][y * 2 + 1];
			let v3 = array[x * 2 + 1][y * 2 + 1];

			// symbolic pooling: majority vote
			let sum = v0 + v1 + v2 + v3;
			result[x][y] = sum > 1 ? 1 : 0; 
			//result[x][y] = sum%2;
		}
	}
	return result;
}
