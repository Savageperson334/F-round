// sanitize
//
// Copied verbatim from https://github.com/karam-ajaj/atlas
//   file data/react-ui/src/api.js, line 65
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Graphs and networks
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function sanitize(base) {
  // Remove trailing slash (except keep '/api' as path root)
  if (base.endsWith("/")) return base.slice(0, -1);
  return base;
}
