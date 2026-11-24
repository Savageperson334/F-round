// sortf
//
// Copied verbatim from https://github.com/xcontcom/neuroparticles
//   file 11x11.js, line 121
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Artificial life
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function sortf(c, d) {
	if (c[1] < d[1]) return 1;
	else if (c[1] > d[1]) return -1;
	else return 0;
}
