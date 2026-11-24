// noteName
//
// Copied verbatim from https://github.com/amacias/octo-vave
//   file web/fm1keys.js, line 18
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"];


const noteName = (n) => NAMES[n % 12] + (Math.floor(n / 12) - 1);
