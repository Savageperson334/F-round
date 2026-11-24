// trimExtension
//
// Copied verbatim from https://github.com/magicshifter/ms4000
//   file web/app/src/utils/files.js, line 1
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function trimExtension(name) {
  return name.replace(/\..+$/, '');
}
