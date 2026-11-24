// skyPathBounds
//
// Copied verbatim from https://github.com/Chienlin1014/Orrery
//   file explainer.js, line 164
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function skyPathBounds(path, unwrapped, marginFraction = 0.12) {
  const minLon = Math.min(...unwrapped);
  const maxLon = Math.max(...unwrapped);
  const minLat = Math.min(...path.map((p) => p.latitude));
  const maxLat = Math.max(...path.map((p) => p.latitude));
  const lonPad = Math.max((maxLon - minLon) * marginFraction, 0.5);
  const latPad = Math.max((maxLat - minLat) * marginFraction, 0.5);
  return {
    minLon: minLon - lonPad,
    maxLon: maxLon + lonPad,
    minLat: minLat - latPad,
    maxLat: maxLat + latPad,
  };
}
