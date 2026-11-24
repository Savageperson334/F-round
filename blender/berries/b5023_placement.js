// placement
//
// Copied verbatim from https://github.com/fenderberg/fm1-sy1
//   file app/site/manager/library.js, line 39
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function placement(first, count, occupied, append=false) {
  const start=Math.min(1024,Math.max(1,Number.parseInt(first,10)||1));
  const end=start+count-1;
  let overlaps=0;
  for(let slot=start;slot<=Math.min(end,1024);slot++) if(occupied.has(slot))overlaps++;
  return {start,end,overlaps,fits:count>0&&end<=1024&&(!append||overlaps===0)};
}
