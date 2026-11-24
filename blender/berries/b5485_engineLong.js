// engineLong
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/editor/labels.js, line 261
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const ENGINE_BY = {
  WAVE: { POS: "POSITION", BEND: "PHASE BEND", SYNC: "HARD SYNC" },
  PHYS: { BEND: "PITCH DROP" },                        // (owner 2026-10-25: POSITION on both unit and editor; BEND is PITCH DROP on the DRUM model, as the unit; WAVE keeps its BEND)
  PHYSICAL: { BEND: "PITCH DROP" },                    // (the engine's shown name: layout.js engineLabel)
  VOICE: { RAND: "RANDOM VOWEL" },
  PHASE: { WAVE: "WAVE 1", WAVE2: "WAVE 2", "WAVE 1": "WAVE 1", "WAVE 2": "WAVE 2" },   // (owner, 0.2.25 evening: WAVE 1 and WAVE 2, as the unit)
  TRIO: { MODE: "FILTER MODE" },                       // (T0229: the one engine card holds the oscillators and the filter: MODE alone would not say whose)
  FM6: { SLOT: "SOURCE" },
};

const ENGINE_COMMON = {
  WAVE: "WAVEFORM", WAVE2: "WAVEFORM 2", DTN: "DETUNE", MIX: "MIX", NOIS: "NOISE", CUT: "CUTOFF", RES: "RESONANCE", DRV: "DRIVE", KTR: "KEY TRACK",
  SYNC: "SYNC", SUB: "SUB", STEPS: "STEPS", DCW: "WAVE SHAPING", ENV: "SHAPING ENV", LINE: "LINE MODE", BITS: "MODEL", "PULSE WIDTH": "PULSE WIDTH",
  CRSH: "CRUSH", SWP: "SWEEP", VIB: "VIBRATO", ARP: "ARPEGGIO", TONE: "TONE", DCY: "DECAY", VOWL: "VOWEL", VOWL2: "VOWEL 2", "VOWL 1": "VOWEL 1", "VOWL 2": "VOWEL 2",
  TALK: "TALK TIME", SHIFT: "FORMANT SHIFT", BUZZ: "BUZZ", BRTH: "BREATH", Q: "RESONANCE", RAND: "RANDOM", INT2: "OSC 2 INTERVAL", INT3: "OSC 3 INTERVAL", MODE: "MODE",
  PW: "PULSE WIDTH", REG: "BARS", BODY: "BODY", TOP: "TOP", PERC: "PERCUSSION", CLICK: "KEY CLICK", ROTR: "ROTARY SPEAKER", MODEL: "MODEL", STRC: "TEXTURE",
  BRIT: "BRIGHT", DAMP: "DAMPING", POS: "POSITION", ACC: "ACCENT", BOW: "BOW", EXC: "EXCITER MIX", HARM: "HARMONICS", BEND: "BEND", CHRD: "CHORD", SYMP: "STRINGS",
  COLR: "COLOR", FREQ: "FREQUENCY", TRK: "KEY TRACK", DENS: "DENSITY", DRFT: "DRIFT", LEN: "LENGTH", CLK: "CLOCK", ALG: "ALGORITHM", FB: "FEEDBACK",
  MLVL: "MOD LEVEL", MRAT: "MOD RATIO", MEG: "MOD ENV", VMOD: "VELOCITY MOD", DTUN: "DETUNE", SLOT: "SOURCE", TABLE: "TABLE",
};


function engineLong(engName, short) { return ENGINE_BY[engName]?.[short] ?? ENGINE_COMMON[short] ?? short; }
