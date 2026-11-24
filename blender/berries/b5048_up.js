// up
//
// Copied verbatim from https://github.com/freaker2k7/translingual
//   file src/index.js, line 95
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Languages scripts and morphology
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


var tsplit = function(str) {
	return str.split(/[\s\-]/).filter(function(v) { return typeof v !== 'undefined' && v.length; })
};


var up = function(str) {
	return tsplit(str).map(function(v) {
		return v.substr(0, 1).toUpperCase() + v.substr(1);
	}).join(' ');
};
