// runs
//
// Copied verbatim from https://github.com/hopechen067/MapStage
//   file mapstage/runtime/qa.mjs, line 50
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Historic cartography
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function runs(flags) {
  const out = [];
  let from = -1;
  for (let i = 0; i <= flags.length; i++) {
    if (i < flags.length && flags[i]) { if (from < 0) from = i; }
    else if (from >= 0) { out.push([from, i - 1]); from = -1; }
  }
  return out;
}
