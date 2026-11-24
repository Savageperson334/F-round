// centuriesSinceJ2000
//
// Copied verbatim from https://github.com/Chienlin1014/Orrery
//   file time.js, line 176
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const J2000 = 2451545.0;

const DAYS_PER_CENTURY = 36525;


function centuriesSinceJ2000(jd) {
  return (jd - J2000) / DAYS_PER_CENTURY;
}
