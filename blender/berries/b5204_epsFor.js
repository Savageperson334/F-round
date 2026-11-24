// epsFor
//
// Copied verbatim from https://github.com/hopechen067/MapStage
//   file mapstage/tuner/scripts/simplify-landcover-globe.mjs, line 146
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Historic cartography
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const ISLAND_SPAN = 3.2;

const FINE_BOXES = [
  { b: [119.1, 21.7, 122.3, 25.6], min: 0.006 },
  { b: [108.4, 17.9, 111.6, 20.6], min: 0.006 },
  { b: [116.6, 22.4, 120.9, 27.7], min: 0.01 },
  { b: [129.0, 30.0, 146.0, 45.8], min: 0.012 },
  { b: [119.0, 5.0, 127.0, 19.2], min: 0.012 },
  { b: [124.4, 33.0, 129.8, 38.8], min: 0.01 },
  { b: [102.0, 8.2, 110.0, 23.4], min: 0.012 },
];


function bboxSpan(ring) {
  let minX = 180;
  let minY = 90;
  let maxX = -180;
  let maxY = -90;
  for (let i = 0; i < ring.length; i++) {
    const p = ring[i];
    if (p[0] < minX) minX = p[0];
    if (p[0] > maxX) maxX = p[0];
    if (p[1] < minY) minY = p[1];
    if (p[1] > maxY) maxY = p[1];
  }
  return Math.max(maxX - minX, maxY - minY);
}


function centroidOf(ring) {
  let x = 0;
  let y = 0;
  const body = ring.slice(0, -1);
  const n = body.length || 1;
  for (let i = 0; i < body.length; i++) {
    x += body[i][0];
    y += body[i][1];
  }
  return [x / n, y / n];
}


function inFineBox(lng, lat) {
  for (let i = 0; i < FINE_BOXES.length; i++) {
    const b = FINE_BOXES[i].b;
    if (lng >= b[0] && lng <= b[2] && lat >= b[1] && lat <= b[3]) return FINE_BOXES[i];
  }
  return null;
}


function epsFor(ring, kind) {
  const span = Math.max(bboxSpan(ring), 0.08);
  const c = centroidOf(ring);
  const fine = inFineBox(c[0], c[1]);
  if (kind === 'urban_area') return Math.min(0.05, Math.max(0.02, span * 0.06));
  if (fine || span <= ISLAND_SPAN) return Math.min(0.06, Math.max(0.028, span * 0.038));
  if (span <= 12) return 0.16;
  return 0.22;
}
