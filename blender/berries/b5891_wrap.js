// wrap
//
// Copied verbatim from https://github.com/sn3p/Orrery
//   file src/js/asteroidOrbits.js, line 10
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//   the same function also appears in: sn3p/Orrery3D
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const TAU = 2 * Math.PI;


const wrap = value => value - TAU * Math.floor((value + Math.PI) / TAU);
