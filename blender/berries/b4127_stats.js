// stats
//
// Copied verbatim from https://github.com/Agerbi-Nouha/beehive-monitoring-app
//   file backend/src/routes/export.js, line 26
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Beehives and unusual agriculture
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function stats(values) {
  const nums = values.filter((v) => typeof v === 'number');
  if (!nums.length) return null;
  const min = Math.min(...nums);
  const max = Math.max(...nums);
  const avg = nums.reduce((s, v) => s + v, 0) / nums.length;
  return { min, max, avg };
}
