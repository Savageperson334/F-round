// engineTip
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/editor/labels.js, line 262
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const ENGINE_TIP = {
  FM6: {
    ALG: "Algorithm: 0 uses the voice's own algorithm, 1 to 32 another one (how the six operators are connected).",
    FB: "Offset on the voice's feedback.", MLVL: "Offset on the output level of the modulator operators (brightness).",
    MRAT: "Offset on the frequency ratio of the modulator operators.", MEG: "Offset on the ENV times of the modulator operators.",
    VMOD: "How much velocity moves the modulator levels.", DTUN: "Detune of the operators against each other.",
    SLOT: "Where this part's FM6 voice comes from: a factory voice (F1 to F11), the part's OWN voice (edited in the ENGINE tab's OPERATORS editor or on the unit, saved with the patch), or a voice of the bank (B1 to B32).",
  },
  WAVE: { TABLE: "The wavetable this part plays: a factory table, or USER 1 to 3 (your own, imported from a WAV file on the WAVETABLES tab; an empty one is marked EMPTY).",
          STEPS: "Rounds the scan position POS to 2 to 19 places across the table, so it steps from frame to frame instead of gliding. OFF is the smooth scan." },
};

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


function engineTip(engName, short) { return ENGINE_TIP[engName]?.[short] ?? `${engName} engine: ${engineLong(engName, short).toLowerCase()}.`; }
