// reassigned
//
// Copied verbatim from https://github.com/graphoflife/GraphOfLife
//   file tools/flowmodules_cli.js, line 122
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Artificial life
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function reassigned(frame, random) {
  const allocations = ((frame.decisions || {}).allocations || []).map(record => {
    const others = [];
    record.targets.forEach((target, i) => { if (target !== record.agent) others.push(i); });
    const alloc = record.alloc.slice();
    for (let k = others.length - 1; k > 0; k--) {
      const j = Math.floor(random() * (k + 1));
      [alloc[others[k]], alloc[others[j]]] = [alloc[others[j]], alloc[others[k]]];
    }
    return { ...record, alloc };
  });
  return { ...frame, decisions: { ...frame.decisions, allocations } };
}
