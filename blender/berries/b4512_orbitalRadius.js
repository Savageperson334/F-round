// orbitalRadius
//
// Copied verbatim from https://github.com/TerjeRu/orrery
//   file shared/src/kepler.js, line 67
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function orbitalRadius(semiMajorAxis, eccentricity, eccentricAnomalyRad) {
  return semiMajorAxis * (1 - eccentricity * Math.cos(eccentricAnomalyRad));
}
