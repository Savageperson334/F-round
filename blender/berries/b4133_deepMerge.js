// deepMerge
//
// Copied verbatim from https://github.com/Agerbi-Nouha/beehive-monitoring-app
//   file backend/src/utils/settingsService.js, line 3
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Beehives and unusual agriculture
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function deepMerge(base, override) {
  if (override === null || typeof override === 'undefined') return base;
  if (Array.isArray(base) && Array.isArray(override)) return override;
  if (typeof base === 'object' && base && typeof override === 'object' && override) {
    const out = { ...base };
    for (const key of Object.keys(override)) {
      out[key] = deepMerge(base?.[key], override[key]);
    }
    return out;
  }
  return override;
}
