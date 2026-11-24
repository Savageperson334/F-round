// redact
//
// Copied verbatim from https://github.com/Vishnu-tppr/motionloom-studio
//   file engine/src/claude-context.js, line 38
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Generative typography and glyphs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const REDACTED_KEYS = Object.freeze(['token', 'apiKey', 'api_key', 'secret', 'password', 'env']);


function isRecord(value) {
  return Boolean(value) && typeof value === 'object' && !Array.isArray(value);
}


function redact(value) {
  if (Array.isArray(value)) return /** @type {any} */ (value.map(redact));
  if (!isRecord(value)) return value;
  /** @type {Record<string, unknown>} */
  const out = {};
  for (const [key, entry] of Object.entries(value)) {
    if (REDACTED_KEYS.includes(key)) continue;
    out[key] = redact(entry);
  }
  return /** @type {T} */ (/** @type {unknown} */ (out));
}
