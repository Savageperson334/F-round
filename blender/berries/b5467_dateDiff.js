// dateDiff
//
// Copied verbatim from https://github.com/ofrohn/d3-orrery
//   file src/util.js, line 65
//   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function dateDiff(dt1, dt2, type) {
  if (!dt2 || !dt1) return; 
  var diff = dt2.valueOf() - dt1.valueOf(),
      tp = type || "d";
  switch (tp) {
    case 'y': case 'yr': diff /= 31556926080; break;
    case 'm': case 'mo': diff /= 2629800000; break;
    case 'd': case 'dy': diff /= 86400000; break;
    case 'h': case 'hr': diff /= 3600000; break;
    case 'n': case 'mn': diff /= 60000; break;
    case 's': case 'sec': diff /= 1000; break;
    case 'ms': break;
  }
  if (type) return Math.floor(diff);
  return diff;
}
