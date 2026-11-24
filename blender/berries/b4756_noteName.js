// noteName
//
// Copied verbatim from https://github.com/amacias/octo-vave
//   file web/app.js, line 36
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"];


const noteName = (n) => NOTE_NAMES[n % 12] + (Math.floor(n / 12) - 1);
