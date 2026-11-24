// dropRingEntries
//
// Copied verbatim from https://github.com/TerjeRu/orrery
//   file watcher/src/body-tree.js, line 28
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function dropRingEntries(chain) {
  return chain.filter((entry) => entry.type !== 'Ring');
}
