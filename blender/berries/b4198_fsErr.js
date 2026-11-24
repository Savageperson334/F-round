// fsErr
//
// Copied verbatim from https://github.com/EndlessPixel/4004-retro-computer
//   file system.js, line 190
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Retro computing
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const FS_ERR = {
  'no such file': 'No such file or directory',
  'no such directory': 'No such file or directory',
  'is a directory': 'Is a directory'
};


const fsErr = e => FS_ERR[e] || e.charAt(0).toUpperCase() + e.slice(1);
