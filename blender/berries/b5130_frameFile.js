// frameFile
//
// Copied verbatim from https://github.com/hopechen067/MapStage
//   file mapstage/runtime/shoot.mjs, line 43
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Historic cartography
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function frameFile(layer, index, ext) {
  const prefix = { full: 'f', map: 'm', hud: 'h' }[layer];
  const e = layer === 'hud' ? 'png' : ext;
  return prefix + String(index).padStart(5, '0') + '.' + e;
}
