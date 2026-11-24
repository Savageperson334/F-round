// uint
//
// Copied verbatim from https://github.com/sn3p/Orrery
//   file src/unified/catalog/contract.js, line 8
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//   the same function also appears in: sn3p/Orrery3D
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const uint = value => Number.isSafeInteger(value) && value >= 0;
