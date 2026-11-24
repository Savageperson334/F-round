// discoveryCount
//
// Copied verbatim from https://github.com/sn3p/Orrery
//   file src/js/asteroidOrbits.js, line 90
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function discoveryCount(dates, jed) {
  let lo = 0, hi = dates.length;
  while (lo < hi) {
    const mid = Math.floor((lo + hi) / 2);
    if (dates[mid] <= jed) lo = mid + 1;
    else hi = mid;
  }
  return lo;
}
