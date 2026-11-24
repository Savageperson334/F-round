// cleanName
//
// Copied verbatim from https://github.com/marksweiss/tastywaves
//   file tools/web/vwlink.js, line 64
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function cleanName(name) {
  const s = name.toUpperCase().replace(/[^A-Z0-9 ._-]/g, '').slice(0, 8).trim();
  return s || 'USER';
}
