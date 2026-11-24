// pct
//
// Copied verbatim from https://github.com/forkwiki/fork
//   file netlify/functions/launch.mjs, line 79
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Archaeology, caves, museums, archival fragments
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const pct = bps => `${(bps / 100).toFixed(bps % 100 ? 1 : 0)}%`;
