// visibleFromTallies
//
// Copied verbatim from https://github.com/sn3p/Orrery
//   file src/unified/catalog/population.js, line 207
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const CLASS_COUNT = 9;

const ALL_MASK = (1 << CLASS_COUNT) - 1;

const CLASS_NEA = 1;

const CLASS_HUNGARIA = 8;

const CLASS_BELT_INNER = 4;

const CLASS_BELT_MIDDLE = 5;

const CLASS_BELT_OUTER = 6;

const BELT_MASK = (1 << CLASS_BELT_INNER) | (1 << CLASS_BELT_MIDDLE) | (1 << CLASS_BELT_OUTER);

const CLASS_HILDA = 7;

const CLASS_TROJAN = 2;

const CLASS_DISTANT = 3;

const PRESET_MASKS = {
  all: ALL_MASK,
  nea: 1 << CLASS_NEA,
  hungarias: 1 << CLASS_HUNGARIA,
  belt: BELT_MASK,
  "belt-inner": 1 << CLASS_BELT_INNER,
  "belt-middle": 1 << CLASS_BELT_MIDDLE,
  "belt-outer": 1 << CLASS_BELT_OUTER,
  hildas: 1 << CLASS_HILDA,
  trojans: 1 << CLASS_TROJAN,
  distant: 1 << CLASS_DISTANT,
  "without-belt": ALL_MASK ^ BELT_MASK,
};

const DEFAULT_POPULATION_PRESET = "all";


function populationMask(preset) {
  return PRESET_MASKS[preset] ?? PRESET_MASKS[DEFAULT_POPULATION_PRESET];
}


function visibleFromTallies(tallies, preset) {
  const mask = populationMask(preset);
  let count = 0;
  for (let id = 0; id < CLASS_COUNT; id++) {
    if (mask & (1 << id)) count += tallies[id];
  }
  return count;
}
