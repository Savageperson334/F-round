// isIndex
//
// Copied verbatim from https://github.com/pshenok/server-survival
//   file src/ui/share.js, line 124
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Public transport and city motion
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const isIndex = (n, len) => Number.isInteger(n) && n >= 0 && n < len;
