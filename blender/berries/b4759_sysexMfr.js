// sysexMfr
//
// Copied verbatim from https://github.com/amacias/octo-vave
//   file web/app.js, line 280
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const SYSEX_MFR = {
  "01": "Sequential", "04": "Moog", "06": "Lexicon", "07": "Kurzweil", "0F": "Ensoniq", "10": "Oberheim",
  "11": "Apple", "18": "E-mu", "1C": "Eventide", "40": "Kawai", "41": "Roland", "42": "Korg", "43": "Yamaha",
  "44": "Casio", "47": "Akai", "52": "Zoom", "7D": "Non-commercial", "7E": "Universal Non-Real Time",
  "7F": "Universal Real Time",
  "00 00 0E": "Alesis", "00 20 1F": "TC Electronic", "00 20 29": "Focusrite/Novation", "00 20 32": "Behringer",
  "00 20 33": "Access", "00 20 3C": "Elektron", "00 20 6B": "Arturia", "00 21 09": "Native Instruments",
};


const hex = (bytes) => [...bytes].map((b) => b.toString(16).padStart(2, "0").toUpperCase()).join(" ");


function sysexMfr(d, i = 1) {
  const id = d[i] === 0 ? hex(d.slice(i, i + 3)) : hex([d[i] ?? 0]);
  return { id, name: SYSEX_MFR[id] || "unknown maker", len: d[i] === 0 ? 3 : 1 };
}
