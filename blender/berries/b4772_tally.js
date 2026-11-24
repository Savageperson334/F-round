// tally
//
// Copied verbatim from https://github.com/amacias/octo-vave
//   file web/app.js, line 2296
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function tally(steps, total) {
  const v = Object.values(steps).filter((r) => r.result);
  const n = (x) => v.filter((r) => r.result === x).length;
  return `${n("yes")} heard · ${n("no")} not heard · ${n("unsure")} unsure · ${total - v.length} to go`;
}
