// patchKey
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/editor/lrrybackup.js, line 35
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const PATCH_KEY0 = 1000;


const patchKey = (slot) => PATCH_KEY0 + slot;
