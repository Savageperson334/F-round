// toPlainPhrase
//
// Copied verbatim from https://github.com/Mohammad-Mirasadollahi/Attack-Explorer
//   file scripts/rewrite-overview-formula-a2-quality.mjs, line 60
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


function stripTechNoise(text) {
  return String(text || '')
    .replace(/`+/g, '')
    .replace(/\*\*/g, '')
    .replace(/—/g, '-')
    .replace(/\s+/g, ' ')
    .trim();
}


function stripTrailingStops(words) {
  const out = [...words];
  while (out.length > 1 && TRAILING_STOP.has(out[out.length - 1].toLowerCase())) {
    out.pop();
  }
  return out;
}


function toPlainPhrase(title, max = 52) {
  let t = stripTechNoise(title);
  t = t.replace(/\s*\((?:CVE|T\d)[^)]*\)\s*/gi, ' ');
  t = t.replace(/\s*\([^)]{0,100}\)\s*/g, ' ');
  t = t.replace(/\.{3,}/g, ' ');
  // Semicolons become Technical Overview clause breaks in the UI.
  t = t.replace(/;/g, ' ');
  t = t.replace(/\s+/g, ' ').trim();
  if (t.includes(' & ')) t = t.split(' & ')[0].trim();
  if (t.includes(', then ')) t = t.split(', then ')[0].trim();
  let words = t.split(/\s+/).filter(Boolean);
  if (words.join(' ').length > max) {
    const out = [];
    for (const w of words) {
      const next = [...out, w].join(' ');
      if (next.length > max) break;
      out.push(w);
    }
    words = out;
  }
  words = stripTrailingStops(words);
  t = words.join(' ') || t.slice(0, max);
  return t.replace(/[.,;:]+$/g, '').trim();
}
