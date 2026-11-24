// storageKey
//
// Copied verbatim from https://github.com/TerjeRu/orrery
//   file ui/src/nicknames.js, line 10
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const STORAGE_PREFIX = 'orrery.nicknames.';


function storageKey(systemAddress) {
  return `${STORAGE_PREFIX}${systemAddress}`;
}
