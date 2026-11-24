// splitPipeline
//
// Copied verbatim from https://github.com/EndlessPixel/4004-retro-computer
//   file shell.js, line 60
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Retro computing
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function splitPipeline(tokens) {
  const parts = [];
  let cur = [];
  for (const t of tokens) {
    if (t === '|') { parts.push(cur); cur = []; }
    else cur.push(t);
  }
  parts.push(cur);
  return parts;
}
