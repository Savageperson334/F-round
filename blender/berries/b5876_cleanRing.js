// cleanRing
//
// Copied verbatim from https://github.com/ridemountainpig/flightcn
//   file scripts/build-world-land.mjs, line 30
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Satellites and orbital systems
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const round = (value) => Math.round(value * 100) / 100;


function cleanRing(ring) {
  const cleaned = [];
  for (const [longitude, latitude] of ring) {
    const point = [round(longitude), round(latitude)];
    const previous = cleaned[cleaned.length - 1];
    if (!previous || previous[0] !== point[0] || previous[1] !== point[1]) {
      cleaned.push(point);
    }
  }
  return cleaned;
}
