// changes
//
// Copied verbatim from https://github.com/fenderberg/fm1-sy1
//   file app/site/manager/library.js, line 120
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function changes(base, slots) {
  const was=new Map(),now=new Set(),writes=[],clears=[]; let added=0,moved=0,edited=0,removed=0;
  base.forEach((it,s)=>{ if(it)was.set(it.uid,s); });
  slots.forEach((it,s)=>{
    if(it){ now.add(it.uid); const from=was.get(it.uid); if(from===undefined)added++; else if(from!==s)moved++; else if(base[s]!==it)edited++; }
    if(it!==base[s])(it?writes:clears).push(s);
  });
  for(const u of was.keys())if(!now.has(u))removed++;
  return {writes,clears,added,moved,edited,removed,total:writes.length+clears.length};
}
