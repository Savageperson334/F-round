// formatBytes
//
// Copied verbatim from https://github.com/graphoflife/GraphOfLife
//   file web/js/api.js, line 249
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Artificial life
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function formatBytes(bytes) {
  if (!bytes) return '0 B';
  const units = ['B', 'KB', 'MB', 'GB', 'TB'];
  const i = Math.min(units.length - 1, Math.floor(Math.log(bytes) / Math.log(1024)));
  return `${(bytes / Math.pow(1024, i)).toFixed(i === 0 ? 0 : 1)} ${units[i]}`;
}
