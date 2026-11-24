// connectCluster
//
// Copied verbatim from https://github.com/tintin0617/mof-visualization-skill
//   file skill/mof-visualization/scripts/cif-core.mjs, line 221
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Molecular shapes and crystal lattices
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const BOND_LIMITS = {
  'C-C': [1.15, 1.75],
  'C-N': [1.10, 1.72],
  'C-O': [1.05, 1.65],
  'N-Zn': [1.75, 2.45],
  'Co-N': [1.75, 2.45],
  'O-Zr': [1.75, 2.55],
};


function pairKey(a, b) {
  return [a, b].sort().join('-');
}


function connectCluster(atoms) {
  const bonds = [];
  for (let first = 0; first < atoms.length; first += 1) {
    for (let second = first + 1; second < atoms.length; second += 1) {
      const limit = BOND_LIMITS[pairKey(atoms[first].element, atoms[second].element)];
      if (!limit) continue;
      const distance = Math.hypot(...atoms[first].p.map((value, axis) => value - atoms[second].p[axis]));
      if (distance >= limit[0] && distance <= limit[1]) bonds.push([first, second]);
    }
  }
  return { atoms, bonds };
}
