// round
//
// Copied verbatim from https://github.com/adamgilman/Orrery
//   file tools/packs/build.mjs, line 206
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const round = (n) => String(Math.round(n * 1000) / 1000);
