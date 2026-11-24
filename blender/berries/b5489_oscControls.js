// oscControls
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/editor/layout.js, line 39
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const LPD = [[], [], [], ["WIDTH"], ["RATIO"], ["DETUNE", "SAWS", "SPREAD"], ["RATIO", "INDEX"], ["AMOUNT"]];


const oscControls = (model) => LPD[Math.min(Math.max(model | 0, 0), 7)].length;
