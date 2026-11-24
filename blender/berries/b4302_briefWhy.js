// briefWhy
//
// Copied verbatim from https://github.com/Mohammad-Mirasadollahi/Attack-Explorer
//   file scripts/rewrite-overview-formula-a2-quality.mjs, line 138
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Sensors and telemetry
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function stripTechNoise(text) {
  return String(text || '')
    .replace(/`+/g, '')
    .replace(/\*\*/g, '')
    .replace(/—/g, '-')
    .replace(/\s+/g, ' ')
    .trim();
}


function briefWhy(step, title) {
  const se = stripTechNoise(step?.simpleExplanation || step?.storyAnalogy || '');
  const clean = (s) =>
    String(s || '')
      .replace(/[.;]/g, ',')
      .replace(/\s+/g, ' ')
      .trim()
      .replace(/[,:]+$/g, '');
  const paren = se.match(/\(([^)]{24,88})\)/);
  if (paren) {
    return clean(paren[1]);
  }
  const first = se.split(/(?<=[.!?])\s+/)[0] || '';
  if (first.length >= 40 && first.length <= 110) {
    return clean(first);
  }
  const label = String(title || 'this stage').toLowerCase().replace(/;/g, ' ');
  return `so the next stage can build on ${label}`;
}
