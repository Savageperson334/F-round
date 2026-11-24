// ccName
//
// Copied verbatim from https://github.com/amacias/octo-vave
//   file web/app.js, line 266
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const CC_NAMES = {
  0: "Bank Select", 1: "Modulation", 2: "Breath", 4: "Foot", 5: "Portamento Time", 6: "Data Entry",
  7: "Volume", 8: "Balance", 10: "Pan", 11: "Expression", 12: "Effect Control 1", 13: "Effect Control 2",
  16: "General Purpose 1", 17: "General Purpose 2", 18: "General Purpose 3", 19: "General Purpose 4",
  64: "Sustain", 65: "Portamento", 66: "Sostenuto", 67: "Soft Pedal", 68: "Legato", 69: "Hold 2",
  70: "Sound Variation", 71: "Resonance", 72: "Release", 73: "Attack", 74: "Cutoff / Brightness",
  75: "Decay", 76: "Vibrato Rate", 77: "Vibrato Depth", 78: "Vibrato Delay", 79: "Sound Controller 10",
  80: "General Purpose 5", 81: "General Purpose 6", 82: "General Purpose 7", 83: "General Purpose 8",
  84: "Portamento Control", 88: "High Res Velocity", 91: "Reverb", 92: "Tremolo", 93: "Chorus",
  94: "Detune", 95: "Phaser", 96: "Data Increment", 97: "Data Decrement", 98: "NRPN LSB", 99: "NRPN MSB",
  100: "RPN LSB", 101: "RPN MSB", 120: "All Sound Off", 121: "Reset All Controllers", 122: "Local Control",
  123: "All Notes Off", 124: "Omni Off", 125: "Omni On", 126: "Mono On", 127: "Poly On",
};


function ccName(cc) {
  if (CC_NAMES[cc]) return CC_NAMES[cc];
  if (cc >= 32 && cc < 64) return CC_NAMES[cc - 32] ? `${CC_NAMES[cc - 32]} LSB` : `LSB of CC ${cc - 32}`;
  return "";
}
