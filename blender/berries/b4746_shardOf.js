// shardOf
//
// Copied verbatim from https://github.com/alexbarakov/amsterdam-by-building
//   file web/app.js, line 2088
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Historic cartography
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const shardOf = key => /^[a-z]/.test(key) ? key[0] : '0';
