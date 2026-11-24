// stripTrailingStops
//
// Copied verbatim from https://github.com/Mohammad-Mirasadollahi/Attack-Explorer
//   file scripts/rewrite-overview-formula-a2-quality.mjs, line 51
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Sensors and telemetry
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const TRAILING_STOP = new Set([
  'the',
  'a',
  'an',
  'into',
  'via',
  'to',
  'of',
  'for',
  'and',
  'or',
  'with',
  'in',
  'on',
  'from',
  'over',
  'as',
  'by',
  'at',
]);


function stripTrailingStops(words) {
  const out = [...words];
  while (out.length > 1 && TRAILING_STOP.has(out[out.length - 1].toLowerCase())) {
    out.pop();
  }
  return out;
}
