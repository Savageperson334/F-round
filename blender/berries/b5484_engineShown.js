// engineShown
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/editor/labels.js, line 260
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const ENGINE_SHOWN = { PHYS: "PHYSICAL" };


const engineShown = (name) => ENGINE_SHOWN[name] ?? name;
