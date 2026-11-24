// keepsOnLoad
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/editor/mockunit.js, line 88
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const KEEP = new Set([0, 39, 40]);


const keepsOnLoad = (id) => KEEP.has(id) || (id >= 17 && id <= 32);
