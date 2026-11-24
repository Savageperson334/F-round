// project
//
// Copied verbatim from https://github.com/graphoflife/GraphOfLife
//   file web/js/sim-worker.js, line 113
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Artificial life
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function project(frame, fields) {
  const out = {};
  for (const name of fields) {
    const dot = name.indexOf('.');
    if (dot < 0) { out[name] = frame[name]; continue; }
    const head = name.slice(0, dot);
    const branch = frame[head];
    if (branch && typeof branch === 'object' && !Array.isArray(branch)) {
      (out[head] ||= {})[name.slice(dot + 1)] = branch[name.slice(dot + 1)];
    }
  }
  return out;
}
