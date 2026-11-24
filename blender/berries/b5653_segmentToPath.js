// segmentToPath
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/convert/svg/drawEdges.js, line 52
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const segmentToPath = (s) => `M${s[0][0]} ${s[0][1]}L${s[1][0]} ${s[1][1]}`;
