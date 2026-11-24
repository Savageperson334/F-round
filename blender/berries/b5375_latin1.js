// latin1
//
// Copied verbatim from https://github.com/marksweiss/tastywaves
//   file tools/web/vwlink.js, line 60
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const latin1 = (b) => String.fromCharCode(...b).replace(/\0+$/, '');
