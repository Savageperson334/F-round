// internalName
//
// Copied verbatim from https://github.com/EndlessPixel/4004-retro-computer
//   file fs.js, line 11
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Retro computing
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const NAME_ALIAS = { '.bash_history': 'bashhist' };


const internalName = name => NAME_ALIAS[name] || name;
