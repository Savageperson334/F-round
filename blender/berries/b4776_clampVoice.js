// clampVoice
//
// Copied verbatim from https://github.com/amacias/octo-vave
//   file web/dx7.js, line 99
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const VOICE_LEN = 156;

const OP_FIELDS = [
  // [offset, key, label, max, group]
  [0, "r1", "Rate 1", 99, "eg"], [1, "r2", "Rate 2", 99, "eg"],
  [2, "r3", "Rate 3", 99, "eg"], [3, "r4", "Rate 4", 99, "eg"],
  [4, "l1", "Level 1", 99, "eg"], [5, "l2", "Level 2", 99, "eg"],
  [6, "l3", "Level 3", 99, "eg"], [7, "l4", "Level 4", 99, "eg"],
  [8, "bp", "Break point", 99, "kbd"], [9, "ld", "L depth", 99, "kbd"],
  [10, "rd", "R depth", 99, "kbd"], [11, "lc", "L curve", 3, "kbd"],
  [12, "rc", "R curve", 3, "kbd"], [13, "rs", "Rate scale", 7, "kbd"],
  [14, "ams", "Amp mod sens", 3, "out"], [15, "vel", "Velocity sens", 7, "out"],
  [16, "out", "Output level", 99, "out"], [17, "mode", "Osc mode", 1, "osc"],
  [18, "coarse", "Coarse", 31, "osc"], [19, "fine", "Fine", 99, "osc"],
  [20, "detune", "Detune", 14, "osc"],
];

const NAME_OFFSET = 145;

const OP_ENABLE = 155;

const GLOBAL_FIELDS = [
  [126, "pr1", "Pitch EG R1", 99, "peg"], [127, "pr2", "Pitch EG R2", 99, "peg"],
  [128, "pr3", "Pitch EG R3", 99, "peg"], [129, "pr4", "Pitch EG R4", 99, "peg"],
  [130, "pl1", "Pitch EG L1", 99, "peg"], [131, "pl2", "Pitch EG L2", 99, "peg"],
  [132, "pl3", "Pitch EG L3", 99, "peg"], [133, "pl4", "Pitch EG L4", 99, "peg"],
  [134, "alg", "Algorithm", 31, "core"], [135, "fb", "Feedback", 7, "core"],
  [136, "oks", "Osc key sync", 1, "core"], [144, "trans", "Transpose", 48, "core"],
  [137, "lspd", "LFO speed", 99, "lfo"], [138, "ldly", "LFO delay", 99, "lfo"],
  [139, "pmd", "Pitch mod depth", 99, "lfo"], [140, "amd", "Amp mod depth", 99, "lfo"],
  [141, "lsync", "LFO key sync", 1, "lfo"], [142, "lwave", "LFO wave", 5, "lfo"],
  [143, "pms", "Pitch mod sens", 7, "lfo"],
];


function paramMax(p) {
  if (p < 126) return OP_FIELDS[p % 21][3];
  if (p >= NAME_OFFSET && p < NAME_OFFSET + 10) return 127;
  if (p === OP_ENABLE) return 63;
  const g = GLOBAL_FIELDS.find((f) => f[0] === p);
  return g ? g[3] : 127;
}


function clampVoice(v) {
  const out = new Array(VOICE_LEN).fill(0);
  for (let p = 0; p < VOICE_LEN; p++) {
    const n = Number(v?.[p]) | 0;
    out[p] = Math.max(0, Math.min(paramMax(p), n));
  }
  return out;
}
