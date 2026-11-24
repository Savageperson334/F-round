// applyCopy
//
// Copied verbatim from https://github.com/Vishnu-tppr/motionloom-studio
//   file engine/src/variants.js, line 185
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Generative typography and glyphs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function applyCopy(controls, variant, scope = '*') {
  const copy = variant?.copy;
  if (!copy) return { ...controls };
  /** @type {Record<string, unknown>} */
  const next = { ...controls };
  for (const [key, value] of Object.entries(controls)) {
    const scoped = copy[`${scope}.${key}`] ?? copy[`*.${key}`];
    if (typeof scoped === 'string') next[key] = scoped;
  }
  return next;
}
