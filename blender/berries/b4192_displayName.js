// displayName
//
// Copied verbatim from https://github.com/EndlessPixel/4004-retro-computer
//   file fs.js, line 12
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Retro computing
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const NAME_DISPLAY = { 'bashhist': '.bash_history' };


const displayName = name => NAME_DISPLAY[name] || name;
