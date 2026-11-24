// clamp
//
// Copied verbatim from https://github.com/PlotterClub/penplotPlayground
//   file src/turtlePlotter.js, line 1
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const clamp = (x, max, min = 0) => Math.max(min, Math.min(max, x));
