// indexMediaModules
//
// Copied verbatim from https://github.com/TonoT/paleontology
//   file src/media-assets.js, line 13
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Fossil measurements and paleontology
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function indexMediaModules(modules) {
  return Object.fromEntries(
    Object.entries(modules).map(([path, url]) => [path.split('/').pop(), url]),
  );
}
